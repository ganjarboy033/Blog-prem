import React from 'react';
import { Download, Copy, Check, Sparkles, Code2, Play, Sliders, HelpCircle, Layers } from 'lucide-react';

interface HeaderProps {
  activeTab: 'simulator' | 'xml' | 'customizer' | 'guide' | 'audit';
  setActiveTab: (tab: 'simulator' | 'xml' | 'customizer' | 'guide' | 'audit') => void;
  onCopyXml: () => void;
  onDownloadXml: () => void;
  copied: boolean;
  fileSizeKb: number;
}

export const Header: React.FC<HeaderProps> = ({
  activeTab,
  setActiveTab,
  onCopyXml,
  onDownloadXml,
  copied,
  fileSizeKb
}) => {
  return (
    <header className="sticky top-0 z-50 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Title */}
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center shadow-lg shadow-cyan-500/25">
              <Code2 className="w-5 h-5 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-lg tracking-tight bg-gradient-to-r from-white via-slate-100 to-cyan-400 bg-clip-text text-transparent">
                  GNZX Blogger Studio
                </span>
                <span className="hidden sm:inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                  <Sparkles className="w-3 h-3" /> 100% Merged &amp; Valid XML
                </span>
              </div>
              <p className="text-xs text-slate-400 hidden sm:block">
                Master 4-in-1 Theme: Stories + 3D Coverflow + Marketplace + 4-Col Gallery + SEO
              </p>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="flex items-center space-x-2 sm:space-x-3">
            <button
              onClick={onCopyXml}
              className={`inline-flex items-center gap-1.5 px-3 py-2 rounded-lg text-xs sm:text-sm font-semibold transition-all ${
                copied
                  ? 'bg-emerald-600 text-white shadow-lg shadow-emerald-600/30'
                  : 'bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700'
              }`}
              title="Salin seluruh kode XML ke clipboard"
            >
              {copied ? <Check className="w-4 h-4 text-white" /> : <Copy className="w-4 h-4 text-cyan-400" />}
              <span>{copied ? 'Tersalin!' : 'Salin XML'}</span>
            </button>

            <button
              onClick={onDownloadXml}
              className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs sm:text-sm font-bold bg-gradient-to-r from-blue-600 to-cyan-500 hover:from-blue-500 hover:to-cyan-400 text-white shadow-lg shadow-cyan-500/20 transition-all hover:scale-[1.02] active:scale-[0.98]"
              title="Unduh file merged_blog_theme.xml"
            >
              <Download className="w-4 h-4" />
              <span className="hidden xs:inline">Unduh .XML</span>
              <span className="text-[10px] opacity-80 font-normal">({fileSizeKb} KB)</span>
            </button>
          </div>
        </div>

        {/* Navigation Tabs */}
        <div className="flex space-x-1 sm:space-x-2 border-t border-slate-800/60 overflow-x-auto py-2 scrollbar-none">
          <button
            onClick={() => setActiveTab('simulator')}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-medium whitespace-nowrap transition-colors ${
              activeTab === 'simulator'
                ? 'bg-cyan-500/15 text-cyan-400 border border-cyan-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
            }`}
          >
            <Play className="w-3.5 h-3.5" />
            <span>Pratinjau Simulator</span>
          </button>

          <button
            onClick={() => setActiveTab('xml')}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-medium whitespace-nowrap transition-colors ${
              activeTab === 'xml'
                ? 'bg-cyan-500/15 text-cyan-400 border border-cyan-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
            }`}
          >
            <Code2 className="w-3.5 h-3.5" />
            <span>Kode XML Lengkap</span>
          </button>

          <button
            onClick={() => setActiveTab('customizer')}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-medium whitespace-nowrap transition-colors ${
              activeTab === 'customizer'
                ? 'bg-cyan-500/15 text-cyan-400 border border-cyan-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
            }`}
          >
            <Sliders className="w-3.5 h-3.5" />
            <span>Kustomisasi Cepat</span>
          </button>

          <button
            onClick={() => setActiveTab('guide')}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-medium whitespace-nowrap transition-colors ${
              activeTab === 'guide'
                ? 'bg-cyan-500/15 text-cyan-400 border border-cyan-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
            }`}
          >
            <HelpCircle className="w-3.5 h-3.5" />
            <span>Panduan Pasang Blog</span>
          </button>

          <button
            onClick={() => setActiveTab('audit')}
            className={`flex items-center gap-2 px-3 py-1.5 rounded-lg text-xs sm:text-sm font-medium whitespace-nowrap transition-colors ${
              activeTab === 'audit'
                ? 'bg-cyan-500/15 text-cyan-400 border border-cyan-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
            }`}
          >
            <Layers className="w-3.5 h-3.5" />
            <span>Audit &amp; Hasil Merge</span>
          </button>
        </div>
      </div>
    </header>
  );
};
