"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Zap, Database, FileText, ChevronRight, X, Maximize2 } from "lucide-react";

interface Source {
  file_name: string;
  page: number;
  excerpt: string;
}


interface ResultsViewProps {
  answer: string;
  sources: Source[];
  latency?: number;
  onSelectedSourcesChange?: (selected: Source[]) => void;
}


export default function ResultsView({ answer, sources, latency, onSelectedSourcesChange }: ResultsViewProps) {
  const [selectedSource, setSelectedSource] = useState<Source | null>(null);
  const [selectedSources, setSelectedSources] = useState<Source[]>([]);

  const handleCheckboxChange = (source: Source, checked: boolean) => {
    let updated: Source[];
    if (checked) {
      updated = [...selectedSources, source];
    } else {
      updated = selectedSources.filter(s => !(s.file_name === source.file_name && s.page === source.page));
    }
    setSelectedSources(updated);
    if (onSelectedSourcesChange) onSelectedSourcesChange(updated);
  };

  // Helper to parse answer and make citations interactive
  const renderAnswer = (text: string) => {
    const parts = text.split(/(\[Source:.*?, Page: \d+\])/g);
    return parts.map((part, i) => {
      const match = part.match(/\[Source:\s*(.*?),\s*Page:\s*(\d+)\]/);
      if (match) {
        const fileName = match[1];
        const pageNum = parseInt(match[2]);
        return (
          <span
            key={i}
            onClick={() => {
              const src = sources.find(s => s.file_name === fileName && s.page === pageNum);
              if (src) setSelectedSource(src);
            }}
            className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded bg-brand-primary/10 border border-brand-primary/20 text-brand-primary text-xs font-mono font-bold cursor-pointer hover:bg-brand-primary/20 transition-colors mx-0.5"
          >
            <FileText className="w-3 h-3" />
            {fileName} (P.{pageNum})
          </span>
        );
      }
      return <span key={i}>{part}</span>;
    });
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="w-full max-w-4xl"
    >
      <div className="glass-panel p-8 rounded-2xl border-brand-primary/20 terminal-glow relative overflow-hidden">
        {/* Answer Header */}
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-display font-bold text-white flex items-center gap-3">
            <Zap className="w-6 h-6 text-brand-primary fill-brand-primary/20" />
            AI Analysis
          </h2>
          {latency && (
            <span className="text-[10px] font-mono text-text-secondary uppercase tracking-widest px-2 py-1 rounded bg-white/5 border border-white/5">
              Processed in {latency}ms
            </span>
          )}
        </div>

        {/* The Answer */}
        <div className="prose prose-invert max-w-none">
          <div className="text-lg text-white/90 leading-relaxed font-sans mb-10 whitespace-pre-wrap">
            {renderAnswer(answer)}
          </div>
        </div>

        {/* Sources Section */}
        <div className="border-t border-white/10 pt-8 mt-2">
          <div className="flex items-center justify-between mb-6">
            <h3 className="text-xs font-mono font-bold uppercase tracking-[0.2em] text-brand-primary flex items-center gap-2">
              <Database className="w-4 h-4" />
              Retrieved Context ({sources.length})
            </h3>
          </div>

          <div className="grid md:grid-cols-2 gap-4">
            {sources.map((source, i) => {
              const checked = selectedSources.some(s => s.file_name === source.file_name && s.page === source.page);
              return (
                <motion.div
                  key={i}
                  whileHover={{ scale: 1.02, border: "1px solid rgba(0, 234, 100, 0.4)" }}
                  className="bg-white/5 border border-white/5 p-5 rounded-xl transition-all group cursor-pointer relative"
                >
                  <input
                    type="checkbox"
                    checked={checked}
                    onChange={e => handleCheckboxChange(source, e.target.checked)}
                    className="absolute top-4 right-4 w-4 h-4 accent-brand-primary z-10"
                    onClick={e => e.stopPropagation()}
                  />
                  <div onClick={() => setSelectedSource(source)}>
                    <div className="flex items-center justify-between mb-3">
                      <div className="flex items-center gap-2">
                        <div className="w-7 h-7 rounded bg-brand-primary/10 flex items-center justify-center">
                          <FileText className="w-4 h-4 text-brand-primary" />
                        </div>
                        <span className="text-sm font-semibold text-white group-hover:text-brand-primary transition-colors">
                          {source.file_name}
                        </span>
                      </div>
                      <span className="text-[10px] font-mono font-bold text-white/30 bg-white/5 px-2 py-1 rounded uppercase tracking-tighter">
                        P. {source.page}
                      </span>
                    </div>
                    <p className="text-xs text-text-secondary leading-relaxed line-clamp-3 italic mb-3">
                      "{source.excerpt}"
                    </p>
                    <div className="flex items-center gap-1 text-[10px] font-bold text-brand-primary opacity-0 group-hover:opacity-100 transition-opacity uppercase tracking-widest">
                      Inspect Source <Maximize2 className="w-3 h-3" />
                    </div>
                  </div>
                </motion.div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Source Modal */}
      <AnimatePresence>
        {selectedSource && (
          <div className="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-background/80 backdrop-blur-md">
            <motion.div
              initial={{ opacity: 0, scale: 0.9, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.9, y: 20 }}
              className="w-full max-w-2xl bg-bg-elevated border border-white/10 rounded-2xl shadow-2xl overflow-hidden"
            >
              <div className="flex items-center justify-between p-6 border-b border-white/5 bg-white/5">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg bg-brand-primary/10 flex items-center justify-center">
                    <FileText className="w-6 h-6 text-brand-primary" />
                  </div>
                  <div>
                    <h4 className="text-lg font-bold text-white">{selectedSource.file_name}</h4>
                    <p className="text-xs text-text-secondary uppercase tracking-widest font-mono">Page {selectedSource.page}</p>
                  </div>
                </div>
                <button 
                  onClick={() => setSelectedSource(null)}
                  className="p-2 hover:bg-white/10 rounded-lg transition-colors text-text-secondary hover:text-white"
                >
                  <X className="w-6 h-6" />
                </button>
              </div>
              <div className="p-8 max-h-[60vh] overflow-y-auto">
                <div className="bg-background/50 rounded-xl p-6 border border-white/5 relative">
                  <span className="absolute -top-3 left-6 px-3 py-1 bg-brand-primary text-text-inverse text-[10px] font-bold rounded uppercase tracking-tighter">
                    Retrieved Chunk
                  </span>
                  <p className="text-white/80 leading-relaxed font-mono text-sm whitespace-pre-wrap italic">
                    "{selectedSource.excerpt}"
                  </p>
                </div>
                <div className="mt-8 flex gap-4">
                  <button className="flex-1 bg-brand-primary text-text-inverse font-bold py-3 rounded-xl hover:opacity-90 transition-opacity">
                    Open Full Document
                  </button>
                  <button 
                    onClick={() => setSelectedSource(null)}
                    className="flex-1 bg-white/5 text-white font-bold py-3 rounded-xl hover:bg-white/10 transition-colors border border-white/10"
                  >
                    Close
                  </button>
                </div>
              </div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
