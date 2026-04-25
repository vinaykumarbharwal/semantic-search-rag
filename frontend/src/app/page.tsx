"use client";

import { useState } from "react";
import SearchHero from "@/components/SearchHero";
import ResultsView from "@/components/ResultsView";
import UploadPortal from "@/components/UploadPortal";
import { motion, AnimatePresence } from "framer-motion";
import { Globe, ExternalLink, ShieldCheck, Database, Zap, Search, Upload } from "lucide-react";

export default function Home() {
  const [activeTab, setActiveTab] = useState<"search" | "ingest">("search");
  const [isSearching, setIsSearching] = useState(false);
  const [results, setResults] = useState<any>(null);

  const handleSearch = async (query: string) => {
    setIsSearching(true);
    setResults(null);
    
    try {
      const response = await fetch(`http://localhost:8000/api/v1/ask?question=${encodeURIComponent(query)}`, {
        method: 'POST'
      });
      const data = await response.json();
      
      if (data.error) {
        alert("Error: " + data.error);
      } else {
        setResults(data);
      }
    } catch (error) {
      console.error("Search failed:", error);
      alert("Failed to connect to the backend server. Make sure it is running on port 8000.");
    } finally {
      setIsSearching(false);
    }
  };

  return (
    <main className="flex-1">
      {/* Navigation */}
      <nav className="fixed top-0 w-full z-50 glass-panel border-b border-white/5">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-brand-primary rounded-lg flex items-center justify-center">
              <Zap className="w-5 h-5 text-text-inverse" />
            </div>
            <span className="font-display font-bold text-xl tracking-tight text-white">
              Cortex
            </span>
          </div>
          <div className="hidden md:flex items-center gap-8">
            {["Platform", "Solutions", "Pricing", "Docs"].map((item) => (
              <a key={item} href="#" className="text-sm font-medium text-text-secondary hover:text-brand-primary transition-colors">
                {item}
              </a>
            ))}
          </div>
          <div className="flex items-center gap-4">
            <button className="text-sm font-semibold text-white px-4 py-2 hover:text-brand-primary transition-colors">
              Sign In
            </button>
            <button className="bg-brand-primary text-text-inverse font-bold px-5 py-2 rounded-lg hover:scale-105 transition-all text-sm">
              Get Started
            </button>
          </div>
        </div>
      </nav>

      {/* Tab Switcher */}
      <div className="flex justify-center mt-24 mb-8">
        <div className="bg-bg-elevated/50 p-1 rounded-xl border border-white/5 flex gap-1">
          <button
            onClick={() => setActiveTab("search")}
            className={`flex items-center gap-2 px-6 py-2.5 rounded-lg text-sm font-bold transition-all ${
              activeTab === "search" ? "bg-brand-primary text-text-inverse" : "text-text-secondary hover:text-white"
            }`}
          >
            <Search className="w-4 h-4" />
            Search
          </button>
          <button
            onClick={() => setActiveTab("ingest")}
            className={`flex items-center gap-2 px-6 py-2.5 rounded-lg text-sm font-bold transition-all ${
              activeTab === "ingest" ? "bg-brand-primary text-text-inverse" : "text-text-secondary hover:text-white"
            }`}
          >
            <Upload className="w-4 h-4" />
            Ingest
          </button>
        </div>
      </div>

      <AnimatePresence mode="wait">
        {activeTab === "search" ? (
          <motion.div
            key="search"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: 20 }}
          >
            <SearchHero onSearch={handleSearch} />

            {/* Results Section */}
            <div className="max-w-4xl mx-auto px-6 pb-20">
              <AnimatePresence>
                {isSearching && (
                  <motion.div
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    className="flex flex-col items-center py-12"
                  >
                    <div className="w-12 h-12 border-4 border-brand-primary/20 border-t-brand-primary rounded-full animate-spin mb-4" />
                    <p className="text-text-secondary font-mono text-sm animate-pulse">Thinking and retrieving context...</p>
                  </motion.div>
                )}

                {results && !isSearching && (
                  <div className="flex justify-center">
                    <ResultsView 
                      answer={results.answer} 
                      sources={results.sources} 
                      latency={results.latency_ms} 
                    />
                  </div>
                )}
              </AnimatePresence>
            </div>
          </motion.div>
        ) : (
          <motion.div
            key="ingest"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            className="pb-32 px-6"
          >
            <UploadPortal />
          </motion.div>
        )}
      </AnimatePresence>

      {/* Trust / Feature Strip */}
      <section className="border-t border-white/5 bg-bg-elevated/30 py-20">
        <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-3 gap-12">
          {[
            { icon: <ShieldCheck />, title: "Enterprise Ready", desc: "SOC2 compliant, secure data isolation, and audit logs." },
            { icon: <Database />, title: "Billion-Scale Indexing", desc: "Powered by FAISS for sub-second retrieval at any volume." },
            { icon: <Zap />, title: "Hybrid Retrieval", desc: "Combines dense vectors with BM25 for maximum precision." },
          ].map((feature, i) => (
            <div key={i} className="flex gap-4">
              <div className="w-12 h-12 shrink-0 bg-brand-primary/10 rounded-xl flex items-center justify-center text-brand-primary">
                {feature.icon}
              </div>
              <div>
                <h3 className="font-display font-bold text-white mb-2">{feature.title}</h3>
                <p className="text-sm text-text-secondary leading-relaxed">{feature.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 border-t border-white/5 px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
          <span className="text-sm text-text-secondary">© 2026 Cortex AI. All rights reserved.</span>
          <div className="flex gap-8">
            <Globe className="w-5 h-5 text-text-secondary hover:text-white transition-colors cursor-pointer" />
            <ExternalLink className="w-5 h-5 text-text-secondary hover:text-white transition-colors cursor-pointer" />
          </div>
        </div>
      </footer>
    </main>
  );
}
