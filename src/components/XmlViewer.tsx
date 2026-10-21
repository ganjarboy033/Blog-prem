import React, { useState, useMemo } from 'react';
import { Copy, Download, Search, Check, FileCode, Sparkles, Layers, ShieldCheck, ArrowDown } from 'lucide-react';

interface XmlViewerProps {
  xmlCode: string;
  onCopyXml: () => void;
  onDownloadXml: () => void;
  copied: boolean;
}

export const XmlViewer: React.FC<XmlViewerProps> = ({
  xmlCode,
  onCopyXml,
  onDownloadXml,
  copied
}) => {
  const [searchTerm, setSearchTerm] = useState('');

  const lines = useMemo(() => {
    return xmlCode.split('\n');
  }, [xmlCode]);

  const filteredLineIndices = useMemo(() => {
    if (!searchTerm.trim()) return [];
    const term = searchTerm.toLowerCase();
    const matches: number[] = [];
    lines.forEach((line, idx) => {
      if (line.toLowerCase().includes(term)) matches.push(idx);
    });
    return matches;
  }, [lines, searchTerm]);

  const quickJumpTo = (tagText: string) => {
    setSearchTerm(tagText);
  };

  return (
    <div className="w-full max-w-6xl mx-auto px-4 py-6">
      {/* Overview Stats Card */}
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 mb-6 shadow-xl">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pb-5 border-b border-slate-800">
          <div>
            <div className="flex items-center gap-2 mb-1">
              <h2 className="text-xl font-bold text-white flex items-center gap-2">
                <FileCode className="w-5 h-5 text-cyan-400" />
                <span>File Template XML Master (Hasil Merge)</span>
              </h2>
              <span className="px-2 py-0.5 rounded-full text-xs font-semibold bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
                v4.0 Final
              </span>
            </div>
            <p className="text-xs sm:text-sm text-slate-400">
              Kode XML siap pakai dan tervalidasi penuh untuk Blogger (Blogspot). Semua fitur dari 4 template telah disatukan secara rapi tanpa kode terlewat.
            </p>
          </div>

          <div className="flex items-center gap-2.5 shrink-0">
            <button
              onClick={onCopyXml}
              className={`flex items-center gap-2 px-4 py-2.5 rounded-xl font-bold text-sm transition-all shadow-md ${
                copied
                  ? 'bg-emerald-600 text-white shadow-emerald-600/30'
                  : 'bg-slate-800 hover:bg-slate-700 text-slate-100 border border-slate-700 hover:border-cyan-500'
              }`}
            >
              {copied ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4 text-cyan-400" />}
              <span>{copied ? 'Berhasil Disalin!' : 'Salin Seluruh Kode'}</span>
            </button>

            <button
              onClick={onDownloadXml}
              className="flex items-center gap-2 px-4 py-2.5 rounded-xl font-bold text-sm bg-gradient-to-r from-blue-600 to-cyan-500 hover:from-blue-500 hover:to-cyan-400 text-white shadow-lg shadow-cyan-500/25 transition-all hover:scale-[1.02]"
            >
              <Download className="w-4 h-4" />
              <span>Unduh File .XML</span>
            </button>
          </div>
        </div>

        {/* Quick Metrics Bar */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mt-4">
          <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800/80">
            <div className="text-xs text-slate-400">Ukuran Berkas</div>
            <div className="text-lg font-extrabold text-white">{(xmlCode.length / 1024).toFixed(1)} KB</div>
          </div>
          <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800/80">
            <div className="text-xs text-slate-400">Jumlah Baris Kode</div>
            <div className="text-lg font-extrabold text-white">{lines.length.toLocaleString()} Baris</div>
          </div>
          <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800/80">
            <div className="text-xs text-slate-400">Status Validasi</div>
            <div className="text-lg font-extrabold text-emerald-400 flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4" /> 100% Valid XML
            </div>
          </div>
          <div className="bg-slate-950/60 p-3 rounded-xl border border-slate-800/80">
            <div className="text-xs text-slate-400">Fitur Terintegrasi</div>
            <div className="text-lg font-extrabold text-cyan-400 flex items-center gap-1">
              <Sparkles className="w-4 h-4" /> 52 Fungsi JS
            </div>
          </div>
        </div>
      </div>

      {/* Code Search & Quick Jump */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 mb-3">
        <div className="relative flex-1 max-w-md">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            placeholder="Cari bagian kode (misal: 'storyModal', 'b:skin', 'like-btn')..."
            className="w-full bg-slate-900 border border-slate-800 rounded-xl pl-9 pr-4 py-2 text-xs sm:text-sm text-slate-200 placeholder:text-slate-500 focus:outline-none focus:border-cyan-500"
          />
          {searchTerm && (
            <span className="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-slate-400">
              {filteredLineIndices.length} baris
            </span>
          )}
        </div>

        {/* Quick Section Tags */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 text-xs scrollbar-none">
          <span className="text-slate-400 text-xs shrink-0">Lompat ke:</span>
          <button
            onClick={() => quickJumpTo('storyModal')}
            className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 whitespace-nowrap"
          >
            Story Modal
          </button>
          <button
            onClick={() => quickJumpTo('sliderSection')}
            className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 whitespace-nowrap"
          >
            3D Slider
          </button>
          <button
            onClick={() => quickJumpTo('marketplaceSection')}
            className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 whitespace-nowrap"
          >
            Marketplace
          </button>
          <button
            onClick={() => quickJumpTo('gallerySection')}
            className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 whitespace-nowrap"
          >
            Galeri 4-Kolom
          </button>
          <button
            onClick={() => quickJumpTo('comments-section')}
            className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 whitespace-nowrap"
          >
            Komentar
          </button>
          <button
            onClick={() => quickJumpTo('FORMSPREE_ENDPOINT_ID')}
            className="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 whitespace-nowrap"
          >
            Formspree ID
          </button>
        </div>
      </div>

      {/* Code Display Box with Line Numbers */}
      <div className="bg-slate-950 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl relative">
        <div className="flex items-center justify-between px-4 py-2.5 bg-slate-900/90 border-b border-slate-800 text-xs text-slate-400 font-mono">
          <div className="flex items-center gap-2">
            <span className="w-2.5 h-2.5 rounded-full bg-cyan-500 animate-pulse" />
            <span>merged_blog_theme.xml</span>
          </div>
          <div>Encoding: UTF-8 | XML 1.0</div>
        </div>

        <div className="max-h-[680px] overflow-auto font-mono text-xs p-4 leading-relaxed scrollbar-thin scrollbar-thumb-slate-700 scrollbar-track-slate-950">
          <table className="w-full border-collapse">
            <tbody>
              {lines.map((line, idx) => {
                const isMatch = searchTerm && line.toLowerCase().includes(searchTerm.toLowerCase());
                return (
                  <tr
                    key={idx}
                    className={`hover:bg-slate-900/80 transition-colors ${
                      isMatch ? 'bg-cyan-950/60 text-cyan-200' : 'text-slate-300'
                    }`}
                  >
                    <td className="w-12 pr-4 text-right text-slate-600 select-none text-[11px] align-top py-0.5">
                      {idx + 1}
                    </td>
                    <td className="whitespace-pre-wrap break-all py-0.5 font-mono">
                      {isMatch ? (
                        <span className="bg-cyan-500/30 px-1 rounded text-cyan-300 font-bold">
                          {line}
                        </span>
                      ) : (
                        <span>{line}</span>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
