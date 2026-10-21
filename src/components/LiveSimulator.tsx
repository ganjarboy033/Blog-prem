import React, { useState } from 'react';
import { Smartphone, Tablet, Monitor, RotateCcw, ExternalLink, Sparkles, Eye, Info } from 'lucide-react';

interface LiveSimulatorProps {
  previewHtml: string;
}

export const LiveSimulator: React.FC<LiveSimulatorProps> = ({ previewHtml }) => {
  const [deviceMode, setDeviceMode] = useState<'mobile' | 'phablet' | 'full'>('phablet');
  const [iframeKey, setIframeKey] = useState(0);

  const reloadSimulator = () => {
    setIframeKey(prev => prev + 1);
  };

  const openInNewTab = () => {
    const newWindow = window.open();
    if (newWindow) {
      newWindow.document.write(previewHtml);
      newWindow.document.close();
    }
  };

  const getFrameWidth = () => {
    switch (deviceMode) {
      case 'mobile':
        return 'w-[390px]';
      case 'phablet':
        return 'w-[500px]';
      case 'full':
        return 'w-full max-w-5xl';
    }
  };

  return (
    <div className="flex flex-col items-center justify-start w-full py-4 px-2 sm:px-6">
      {/* Simulator Control Bar */}
      <div className="w-full max-w-5xl bg-slate-800/80 backdrop-blur border border-slate-700/80 rounded-2xl p-3 mb-4 flex flex-wrap items-center justify-between gap-3 shadow-xl">
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1 bg-slate-900/80 p-1 rounded-xl border border-slate-700">
            <button
              onClick={() => setDeviceMode('mobile')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                deviceMode === 'mobile'
                  ? 'bg-cyan-500 text-white shadow-md'
                  : 'text-slate-400 hover:text-white'
              }`}
              title="Tampilan HP Kompak (390px)"
            >
              <Smartphone className="w-3.5 h-3.5" />
              <span>Mobile (390px)</span>
            </button>

            <button
              onClick={() => setDeviceMode('phablet')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                deviceMode === 'phablet'
                  ? 'bg-cyan-500 text-white shadow-md'
                  : 'text-slate-400 hover:text-white'
              }`}
              title="Tampilan Standar Template (500px)"
            >
              <Tablet className="w-3.5 h-3.5" />
              <span>Phablet (500px)</span>
            </button>

            <button
              onClick={() => setDeviceMode('full')}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-colors ${
                deviceMode === 'full'
                  ? 'bg-cyan-500 text-white shadow-md'
                  : 'text-slate-400 hover:text-white'
              }`}
              title="Tampilan Desktop / Tablet Lebar"
            >
              <Monitor className="w-3.5 h-3.5" />
              <span>Responsif Lebar</span>
            </button>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <button
            onClick={reloadSimulator}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-900/60 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
            title="Muat ulang pratinjau"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>Reload</span>
          </button>

          <button
            onClick={openInNewTab}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium bg-cyan-500/10 hover:bg-cyan-500/20 text-cyan-400 border border-cyan-500/30 transition-colors"
            title="Buka pratinjau penuh di tab baru"
          >
            <ExternalLink className="w-3.5 h-3.5" />
            <span>Buka Tab Baru</span>
          </button>
        </div>
      </div>

      {/* Feature Interaction Hint Pills */}
      <div className="w-full max-w-5xl mb-4 bg-gradient-to-r from-cyan-950/40 via-slate-900/60 to-blue-950/40 border border-cyan-500/20 rounded-xl p-3 text-xs text-slate-300 flex items-start gap-2.5">
        <Sparkles className="w-4 h-4 text-cyan-400 mt-0.5 shrink-0" />
        <div className="space-y-1">
          <p className="font-semibold text-cyan-300">Tips Uji Fitur Interaktif pada Simulator:</p>
          <div className="flex flex-wrap gap-1.5 text-[11px] text-slate-400">
            <span className="bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
              📸 Klik foto Profil untuk memutar Story Status
            </span>
            <span className="bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
              ➕ Klik tombol (+) untuk simpan Story Video/Foto s.d 100MB
            </span>
            <span className="bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
              🎠 Coba Tab Switcher (Semua, 3D Slider, Marketplace, Galeri)
            </span>
            <span className="bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
              🔍 Ketik di input cari untuk filter instan 4-kolom
            </span>
            <span className="bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
              🔊 Buka artikel &amp; klik 'Dengarkan Artikel' untuk Text-to-Speech
            </span>
            <span className="bg-slate-800/80 px-2 py-0.5 rounded border border-slate-700">
              ⚙️ Klik menu titik 3 di kanan atas untuk ganti tema, wallpaper &amp; lofi audio
            </span>
          </div>
        </div>
      </div>

      {/* Device Frame Wrapper */}
      <div
        className={`${getFrameWidth()} transition-all duration-300 ease-in-out relative flex flex-col items-center`}
      >
        {deviceMode !== 'full' ? (
          <div className="w-full bg-slate-950 rounded-[40px] p-3 shadow-2xl border-4 border-slate-800 ring-1 ring-slate-700/50">
            {/* Phone Speaker Notch */}
            <div className="flex justify-center mb-2">
              <div className="w-24 h-4 bg-slate-900 rounded-full flex items-center justify-center gap-1.5">
                <div className="w-2 h-2 rounded-full bg-slate-800" />
                <div className="w-8 h-1.5 rounded-full bg-slate-800" />
              </div>
            </div>

            {/* Screen iframe */}
            <div className="rounded-[30px] overflow-hidden bg-slate-950 h-[760px] relative border border-slate-800/80">
              <iframe
                key={iframeKey}
                title="Blogger Live Simulator"
                srcDoc={previewHtml}
                className="w-full h-full border-none"
                sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals"
              />
            </div>

            {/* Phone Home Bar */}
            <div className="flex justify-center mt-2.5">
              <div className="w-32 h-1 bg-slate-700 rounded-full" />
            </div>
          </div>
        ) : (
          <div className="w-full bg-slate-900 rounded-2xl overflow-hidden border border-slate-800 shadow-2xl h-[800px]">
            <div className="bg-slate-950 px-4 py-2 border-b border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-1.5">
                <div className="w-3 h-3 rounded-full bg-red-500/80" />
                <div className="w-3 h-3 rounded-full bg-amber-500/80" />
                <div className="w-3 h-3 rounded-full bg-emerald-500/80" />
              </div>
              <div className="bg-slate-900 px-6 py-1 rounded-md text-xs text-slate-400 font-mono flex items-center gap-2">
                <Eye className="w-3 h-3 text-cyan-400" />
                <span>https://bagja.dev</span>
              </div>
              <div className="text-[11px] text-slate-500">Live Preview</div>
            </div>
            <iframe
              key={iframeKey}
              title="Blogger Live Simulator"
              srcDoc={previewHtml}
              className="w-full h-[calc(100%-40px)] border-none"
              sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-modals"
            />
          </div>
        )}
      </div>
    </div>
  );
};
