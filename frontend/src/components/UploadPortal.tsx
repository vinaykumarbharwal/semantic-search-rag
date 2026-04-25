"use client";

import { useState, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Upload, File, X, CheckCircle, AlertCircle, Loader2 } from "lucide-react";

export default function UploadPortal() {
  const [files, setFiles] = useState<File[]>([]);
  const [status, setStatus] = useState<"idle" | "uploading" | "success" | "error">("idle");
  const [isDragging, setIsDragging] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFiles(Array.from(e.target.files));
    }
  };

  const removeFile = (index: number) => {
    setFiles(files.filter((_, i) => i !== index));
  };

  const onDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const onDragLeave = () => {
    setIsDragging(false);
  };

  const onDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files) {
      setFiles(Array.from(e.dataTransfer.files));
    }
  };

  const handleUpload = async () => {
    if (files.length === 0) return;
    
    setStatus("uploading");
    
    try {
      const formData = new FormData();
      files.forEach((file) => {
        formData.append("files", file);
      });

      const response = await fetch("http://localhost:8000/api/v1/ingest", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        setStatus("success");
        setFiles([]);
        setTimeout(() => setStatus("idle"), 3000);
      } else {
        setStatus("error");
        alert("Ingestion failed. Please check the backend logs.");
      }
    } catch (error) {
      console.error("Upload failed:", error);
      setStatus("error");
      alert("Failed to connect to the backend server.");
    }
  };

  return (
    <div className="w-full max-w-2xl mx-auto mt-20">
      <div className="flex items-center justify-between mb-6">
        <h3 className="text-xl font-display font-bold text-white flex items-center gap-2">
          <Upload className="w-5 h-5 text-brand-primary" />
          Ingest Documents
        </h3>
        <span className="text-[10px] font-mono text-text-secondary uppercase tracking-widest bg-white/5 px-2 py-1 rounded border border-white/5">
          PDF, TXT, MD supported
        </span>
      </div>

      <div
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onDrop={onDrop}
        className={`relative border-2 border-dashed rounded-2xl p-12 transition-all flex flex-col items-center justify-center ${
          isDragging 
            ? "border-brand-primary bg-brand-primary/5 scale-[1.01]" 
            : "border-white/10 hover:border-white/20 bg-white/[0.02]"
        }`}
      >
        <input
          type="file"
          multiple
          ref={fileInputRef}
          onChange={handleFileChange}
          className="hidden"
          accept=".pdf,.txt,.md"
        />

        <div className="w-16 h-16 bg-brand-primary/10 rounded-full flex items-center justify-center mb-6">
          <Upload className={`w-8 h-8 ${isDragging ? "text-brand-primary animate-bounce" : "text-brand-primary/50"}`} />
        </div>

        <p className="text-lg font-medium text-white mb-2 text-center">
          {isDragging ? "Drop your files here" : "Drag and drop your documents"}
        </p>
        <p className="text-sm text-text-secondary mb-8 text-center">
          Or <button onClick={() => fileInputRef.current?.click()} className="text-brand-primary hover:underline font-bold">browse files</button> from your computer
        </p>

        <AnimatePresence>
          {files.length > 0 && (
            <motion.div 
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              exit={{ opacity: 0, height: 0 }}
              className="w-full space-y-3"
            >
              <div className="pt-6 border-t border-white/10 w-full">
                {files.map((file, i) => (
                  <div key={i} className="flex items-center justify-between bg-white/5 p-3 rounded-lg border border-white/5 mb-2">
                    <div className="flex items-center gap-3">
                      <File className="w-4 h-4 text-brand-primary" />
                      <span className="text-sm text-white font-medium truncate max-w-[300px]">{file.name}</span>
                      <span className="text-[10px] text-text-secondary uppercase">{(file.size / 1024).toFixed(1)} KB</span>
                    </div>
                    <button onClick={() => removeFile(i)} className="text-white/20 hover:text-red-400 transition-colors">
                      <X className="w-4 h-4" />
                    </button>
                  </div>
                ))}
              </div>

              <button
                disabled={status === "uploading"}
                onClick={handleUpload}
                className="w-full bg-brand-primary text-text-inverse font-bold py-3 rounded-xl hover:scale-[1.01] active:scale-95 transition-all flex items-center justify-center gap-2"
              >
                {status === "uploading" ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Processing Pipeline...
                  </>
                ) : (
                  "Start Ingestion"
                )}
              </button>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Success / Error States */}
        <AnimatePresence>
          {status === "success" && (
            <motion.div 
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              className="absolute inset-0 bg-background/90 backdrop-blur-sm rounded-2xl flex flex-col items-center justify-center z-10"
            >
              <div className="w-16 h-16 bg-brand-primary/20 rounded-full flex items-center justify-center mb-4">
                <CheckCircle className="w-8 h-8 text-brand-primary" />
              </div>
              <h4 className="text-xl font-display font-bold text-white mb-2">Ingestion Complete</h4>
              <p className="text-sm text-text-secondary">Your documents are now indexed and searchable.</p>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
