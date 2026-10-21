import React, { useState } from 'react';
import { BlogConfig, DEFAULT_BLOG_CONFIG } from '../data/xmlTemplate';
import { Sliders, Copy, Download, RefreshCw, Check, Sparkles, User, Mail, Globe, Palette, Type, Image } from 'lucide-react';

interface TemplateCustomizerProps {
  config: BlogConfig;
  onChangeConfig: (newConfig: BlogConfig) => void;
  onCopyXml: () => void;
  onDownloadXml: () => void;
  copied: boolean;
}

export const TemplateCustomizer: React.FC<TemplateCustomizerProps> = ({
  config,
  onChangeConfig,
  onCopyXml,
  onDownloadXml,
  copied
}) => {
  const [formData, setFormData] = useState<BlogConfig>(config);

  const handleChange = (field: keyof BlogConfig, value: any) => {
    const updated = { ...formData, [field]: value };
    setFormData(updated);
    onChangeConfig(updated);
  };

  const handleReset = () => {
    setFormData(DEFAULT_BLOG_CONFIG);
    onChangeConfig(DEFAULT_BLOG_CONFIG);
  };

  return (
    <div className="w-full max-w-4xl mx-auto px-4 py-6">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-xl mb-6">
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pb-5 border-b border-slate-800">
          <div>
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              <Sliders className="w-5 h-5 text-cyan-400" />
              <span>Kustomisasi Cepat Template XML</span>
            </h2>
            <p className="text-xs sm:text-sm text-slate-400 mt-1">
              Sesuaikan data identitas blog, akun Formspree, Google Analytics, dan tema default. Perubahan akan otomatis dimasukkan ke dalam kode XML hasil unduhan.
            </p>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={handleReset}
              className="flex items-center gap-1.5 px-3 py-2 rounded-lg text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 transition-colors"
              title="Reset ke pengaturan awal"
            >
              <RefreshCw className="w-3.5 h-3.5" />
              <span>Reset</span>
            </button>

            <button
              onClick={onCopyXml}
              className="flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white shadow-md transition-all"
            >
              {copied ? <Check className="w-4 h-4" /> : <Copy className="w-4 h-4" />}
              <span>{copied ? 'Tersalin' : 'Salin XML'}</span>
            </button>

            <button
              onClick={onDownloadXml}
              className="flex items-center gap-1.5 px-3.5 py-2 rounded-lg text-xs font-bold bg-gradient-to-r from-blue-600 to-cyan-500 text-white shadow-md transition-all hover:scale-[1.02]"
            >
              <Download className="w-4 h-4" />
              <span>Unduh .XML</span>
            </button>
          </div>
        </div>

        {/* Form Fields Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-5 mt-6">
          {/* Author Name */}
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <User className="w-3.5 h-3.5 text-cyan-400" />
              <span>Nama Penulis / Pemilik Blog:</span>
            </label>
            <input
              type="text"
              value={formData.authorName}
              onChange={(e) => handleChange('authorName', e.target.value)}
              placeholder="Contoh: Gandzar Subagja"
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
            />
          </div>

          {/* Email Address */}
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <Mail className="w-3.5 h-3.5 text-cyan-400" />
              <span>Alamat Email Kontak:</span>
            </label>
            <input
              type="email"
              value={formData.email}
              onChange={(e) => handleChange('email', e.target.value)}
              placeholder="Contoh: gandzar@gmail.com"
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
            />
          </div>

          {/* Bio / Tagline */}
          <div className="space-y-1.5 md:col-span-2">
            <label className="text-xs font-semibold text-slate-300">
              Biodata / Slogan Singkat:
            </label>
            <textarea
              value={formData.bio}
              onChange={(e) => handleChange('bio', e.target.value)}
              rows={2}
              placeholder="Contoh: Cuman Konten Kreator & Fullstack Specialist biasa yang suka ngoprek sistem."
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
            />
          </div>

          {/* Formspree Endpoint ID */}
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <Globe className="w-3.5 h-3.5 text-cyan-400" />
              <span>Formspree Endpoint ID (Komentar Email):</span>
            </label>
            <input
              type="text"
              value={formData.formspreeId}
              onChange={(e) => handleChange('formspreeId', e.target.value)}
              placeholder="Contoh: mvkzpprq"
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
            />
            <p className="text-[11px] text-slate-500">
              Daftar gratis di formspree.io untuk menerima notifikasi komentar pengunjung langsung ke email Anda.
            </p>
          </div>

          {/* Google Analytics GA4 ID */}
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <Sparkles className="w-3.5 h-3.5 text-cyan-400" />
              <span>Google Analytics 4 ID (GA4):</span>
            </label>
            <input
              type="text"
              value={formData.ga4Id}
              onChange={(e) => handleChange('ga4Id', e.target.value)}
              placeholder="Contoh: G-XXXXXXXXXX"
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
            />
            <p className="text-[11px] text-slate-500">
              Isi dengan Measurement ID Google Analytics Anda untuk pelacakan trafik akurat.
            </p>
          </div>

          {/* Avatar URL */}
          <div className="space-y-1.5 md:col-span-2">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <Image className="w-3.5 h-3.5 text-cyan-400" />
              <span>URL Foto Avatar Profil (Story Ring):</span>
            </label>
            <input
              type="text"
              value={formData.avatarUrl}
              onChange={(e) => handleChange('avatarUrl', e.target.value)}
              placeholder="https://blogger.googleusercontent.com/..."
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500 font-mono text-xs"
            />
          </div>

          {/* Default Theme Selector */}
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <Palette className="w-3.5 h-3.5 text-cyan-400" />
              <span>Tema Warna Default:</span>
            </label>
            <select
              value={formData.defaultTheme}
              onChange={(e) => handleChange('defaultTheme', e.target.value)}
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
            >
              <option value="default">Default Cyan &amp; Deep Blue</option>
              <option value="sakura">Sakura Pink &amp; Rose</option>
              <option value="cyberpunk">Cyberpunk Neon &amp; Magenta</option>
              <option value="emerald">Emerald Mint &amp; Forest</option>
              <option value="sunset">Sunset Amber &amp; Gold</option>
              <option value="light">Light Cream Mode</option>
            </select>
          </div>

          {/* Default Font Family */}
          <div className="space-y-1.5">
            <label className="text-xs font-semibold text-slate-300 flex items-center gap-1.5">
              <Type className="w-3.5 h-3.5 text-cyan-400" />
              <span>Font Style Default:</span>
            </label>
            <select
              value={formData.defaultFont}
              onChange={(e) => handleChange('defaultFont', e.target.value)}
              className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3.5 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
            >
              <option value="sans">Modern Sans-Serif (Segoe UI / System)</option>
              <option value="serif">Classic Serif (Georgia / Editorial)</option>
              <option value="mono">Developer Mono (Fira Code / Consolas)</option>
              <option value="cursive">Playful Comic (Comic Neue / Chalkboard)</option>
            </select>
          </div>
        </div>

        {/* Live Notification Pill */}
        <div className="mt-6 p-4 rounded-xl bg-cyan-950/30 border border-cyan-500/20 text-xs text-cyan-300 flex items-center justify-between">
          <span>
            ✨ Pengaturan otomatis disinkronkan ke template XML! Klik "Salin XML" atau "Unduh .XML" untuk memasang ke blog Anda.
          </span>
        </div>
      </div>
    </div>
  );
};
