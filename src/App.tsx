/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useMemo } from 'react';
import { Header } from './components/Header';
import { LiveSimulator } from './components/LiveSimulator';
import { XmlViewer } from './components/XmlViewer';
import { TemplateCustomizer } from './components/TemplateCustomizer';
import { InstallationGuide } from './components/InstallationGuide';
import { FeatureAudit } from './components/FeatureAudit';
import { DEFAULT_BLOG_CONFIG, BlogConfig, generateCustomXml } from './data/xmlTemplate';
import { convertXmlToPreviewHtml } from './utils/xmlToPreviewHtml';

export default function App() {
  const [activeTab, setActiveTab] = useState<'simulator' | 'xml' | 'customizer' | 'guide' | 'audit'>('simulator');
  const [blogConfig, setBlogConfig] = useState<BlogConfig>(DEFAULT_BLOG_CONFIG);
  const [copied, setCopied] = useState(false);
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  // Generate current XML based on custom config
  const currentXml = useMemo(() => {
    return generateCustomXml(blogConfig);
  }, [blogConfig]);

  // Generate live HTML for the simulator iframe
  const previewHtml = useMemo(() => {
    return convertXmlToPreviewHtml(currentXml, `${blogConfig.authorName} - Official Blog & Portfolio`);
  }, [currentXml, blogConfig.authorName]);

  const fileSizeKb = useMemo(() => {
    return Math.round(currentXml.length / 1024);
  }, [currentXml]);

  const triggerToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => {
      setToastMessage(null);
    }, 3200);
  };

  const handleCopyXml = async () => {
    try {
      await navigator.clipboard.writeText(currentXml);
      setCopied(true);
      triggerToast('Seluruh kode XML berhasil disalin ke clipboard!');
      setTimeout(() => setCopied(false), 3000);
    } catch {
      // Fallback
      const textarea = document.createElement('textarea');
      textarea.value = currentXml;
      document.body.appendChild(textarea);
      textarea.select();
      document.execCommand('copy');
      document.body.removeChild(textarea);
      setCopied(true);
      triggerToast('Seluruh kode XML berhasil disalin ke clipboard!');
      setTimeout(() => setCopied(false), 3000);
    }
  };

  const handleDownloadXml = () => {
    const blob = new Blob([currentXml], { type: 'application/xml;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'merged_blog_theme.xml';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    triggerToast('File merged_blog_theme.xml berhasil diunduh!');
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-cyan-500 selection:text-white">
      {/* Top Header */}
      <Header
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        onCopyXml={handleCopyXml}
        onDownloadXml={handleDownloadXml}
        copied={copied}
        fileSizeKb={fileSizeKb}
      />

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col">
        {activeTab === 'simulator' && <LiveSimulator previewHtml={previewHtml} />}
        {activeTab === 'xml' && (
          <XmlViewer
            xmlCode={currentXml}
            onCopyXml={handleCopyXml}
            onDownloadXml={handleDownloadXml}
            copied={copied}
          />
        )}
        {activeTab === 'customizer' && (
          <TemplateCustomizer
            config={blogConfig}
            onChangeConfig={setBlogConfig}
            onCopyXml={handleCopyXml}
            onDownloadXml={handleDownloadXml}
            copied={copied}
          />
        )}
        {activeTab === 'guide' && <InstallationGuide />}
        {activeTab === 'audit' && <FeatureAudit />}
      </main>

      {/* Persistent Bottom Bar on Mobile for Instant Action */}
      <div className="sm:hidden sticky bottom-0 z-40 bg-slate-900/95 backdrop-blur-md border-t border-slate-800 p-2.5 flex items-center gap-2">
        <button
          onClick={handleCopyXml}
          className="flex-1 py-2 px-3 rounded-xl bg-slate-800 text-xs font-bold text-slate-200 border border-slate-700 flex items-center justify-center gap-1.5"
        >
          {copied ? 'Tersalin!' : 'Salin XML'}
        </button>
        <button
          onClick={handleDownloadXml}
          className="flex-1 py-2 px-3 rounded-xl bg-gradient-to-r from-blue-600 to-cyan-500 text-xs font-bold text-white flex items-center justify-center gap-1.5 shadow-md shadow-cyan-500/20"
        >
          Unduh .XML ({fileSizeKb}KB)
        </button>
      </div>

      {/* Global Floating Toast */}
      {toastMessage && (
        <div className="fixed bottom-16 sm:bottom-6 left-1/2 -translate-x-1/2 z-50 pointer-events-none">
          <div className="bg-slate-900/95 text-white border border-cyan-500/40 px-4 py-2.5 rounded-full text-xs font-semibold shadow-2xl backdrop-blur-lg flex items-center gap-2 animate-bounce">
            <span className="w-2 h-2 rounded-full bg-cyan-400" />
            <span>{toastMessage}</span>
          </div>
        </div>
      )}
    </div>
  );
}
