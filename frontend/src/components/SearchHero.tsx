"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { Search, Command, Zap, Terminal } from "lucide-react";

export default function SearchHero({ onSearch }: { onSearch: (q: str) => void }) {
  const [query, setQuery] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim()) onSearch(query);
  };

  return (
    <section className="relative pt-20 pb-32 px-6 flex flex-col items-center justify-center overflow-hidden">
      {/* Background Hexagon Pattern / Glow */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-full -z-10 opacity-30">
        <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[600px] h-[600px] bg-brand-primary/20 blur-[120px] rounded-full" />
      </div>

      {/* Eyebrow Tag */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="flex items-center gap-2 px-3 py-1 rounded-full border border-brand-primary/30 bg-brand-primary/5 mb-8"
      >
        <Zap className="w-3.5 h-3.5 text-brand-primary" />
        <span className="text-[11px] font-mono font-semibold uppercase tracking-wider text-brand-primary">
          #1 Technical Knowledge Assistant
        </span>
      </motion.div>

      {/* Main Headline */}
      <motion.h1
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="text-5xl md:text-7xl font-display font-extrabold text-center max-w-4xl mb-6 tracking-tight"
      >
        Search with <span className="text-brand-primary">Meaning</span>. <br />
        Answer with <span className="text-brand-primary">Precision</span>.
      </motion.h1>

      <motion.p
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="text-text-secondary text-lg md:text-xl text-center max-w-2xl mb-12"
      >
        An enterprise-grade RAG system that understands your documents like a senior engineer. 
        Ask anything, get cited answers in seconds.
      </motion.p>

      {/* Search Bar (Terminal Style) */}
      <motion.form
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.3 }}
        onSubmit={handleSubmit}
        className="w-full max-w-3xl relative group"
      >
        <div className="absolute -inset-1 bg-gradient-to-r from-brand-primary/50 to-blue-500/50 rounded-2xl blur opacity-25 group-hover:opacity-40 transition duration-1000 group-hover:duration-200" />
        
        <div className="relative flex items-center bg-bg-elevated/90 border border-white/10 rounded-xl p-2 pl-6 backdrop-blur-xl">
          <Terminal className="w-5 h-5 text-brand-primary mr-4 opacity-70" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask a technical question or search documents..."
            className="flex-1 bg-transparent border-none outline-none text-white font-sans text-lg py-3 placeholder:text-white/20"
          />
          <div className="hidden md:flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-white/5 border border-white/5 mr-2">
            <Command className="w-3.5 h-3.5 text-white/40" />
            <span className="text-xs font-medium text-white/40">K</span>
          </div>
          <button
            type="submit"
            className="bg-brand-primary text-text-inverse font-bold px-6 py-3 rounded-lg hover:scale-[1.02] active:scale-95 transition-all terminal-glow"
          >
            Ask AI
          </button>
        </div>
      </motion.form>

      {/* Quick Stats / Social Proof */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-8 md:gap-16 items-center"
      >
        {[
          { label: "Search Latency", value: "< 200ms" },
          { label: "Accuracy (RAGAS)", value: "94%" },
          { label: "Vector Index", value: "10M+" },
          { label: "LLM Backend", value: "Claude/GPT" },
        ].map((stat, i) => (
          <div key={i} className="flex flex-col items-center">
            <span className="text-2xl font-display font-bold text-white mb-1">{stat.value}</span>
            <span className="text-[10px] uppercase tracking-widest text-text-secondary font-mono">{stat.label}</span>
          </div>
        ))}
      </motion.div>
    </section>
  );
}
