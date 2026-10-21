#!/usr/bin/env python3
"""
Generator for the Ultimate Merged Blogger XML Theme.
Merges:
1. 2_31be271e.xml (Stories IndexedDB system)
2. hebat_Copy__8e18c959.xml (3D Coverflow slider, glowing borders, themes, particle FX, 404 page, audio player, traffic)
3. hebat_Copy__Copy__8fa96916.xml (Marketplace horizontal snap carousel)
4. hebat_sekali_5ef1444b.xml (4-column photo gallery grid + instant search)
+ Premium enhancements:
- SEO Structured Data (JSON-LD, OpenGraph, Twitter Cards, Canonical, Preconnect)
- Reading Time Estimator
- Text-to-Speech (TTS) Voice Reader for blog articles
- Multi-view Switcher Tabs (All, 3D Slider, Marketplace, 4-Col Gallery)
- Modern Responsive Comment System (Formspree + LocalStorage fallback + reaction hearts + reply indicator + edit/delete)
- Glassmorphism Floating Toast Notifications
- Tag/Category Filter Pills
- Fallback mock data when running in simulator/preview mode
"""

import os

XML_CONTENT = '''<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:css='false' b:defaultwidgetversion='2' b:layoutsVersion='3' b:responsive='true' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
  <head>
    <meta content='width=device-width, initial-scale=1, maximum-scale=5' name='viewport'/>
    <meta charset='UTF-8'/>
    <title><data:view.title.escaped/></title>
    
    <!-- SEO & Metadata Primordial -->
    <meta content='IE=edge' http-equiv='X-UA-Compatible'/>
    <meta content='id' name='language'/>
    <meta content='Indonesia' name='geo.country'/>
    <meta content='Gandzar Subagja' name='author'/>
    <meta content='summary_large_image' name='twitter:card'/>
    <meta expr:content='data:view.title.escaped' property='og:title'/>
    <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
    <meta content='website' property='og:type'/>
    <meta expr:content='data:view.description.escaped' property='og:description'/>
    <meta expr:content='data:view.description.escaped' name='description'/>
    
    <b:if cond='data:view.featuredImage'>
      <meta expr:content='data:view.featuredImage' property='og:image'/>
      <meta expr:content='data:view.featuredImage' name='twitter:image'/>
    <b:else/>
      <meta content='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQr_6Q2B6xIcyzYVfd3D5QpeH0YVaPzGM01Wgsp7msgcZ7X-dKoIdhdOFpO0gWdSxdaZhU-Tzzy_GyA39GF6svcSW9UK-1E39kZMqMjoNizs-Nv65xy_aY6vaFNh4MNiw5q5XphZbilf5uH6DUxQ0oMaGLMDtMK1E34r1GW5FCGVM0hskGWexFUDSZ7RA/s800/icon_untukdi_aboutthisapp.webp' property='og:image'/>
    </b:if>

    <!-- Preconnect & DNS-Prefetch untuk Kecepatan Loading Maksimal -->
    <link href='https://cdnjs.cloudflare.com' rel='preconnect'/>
    <link href='https://cdnjs.cloudflare.com' rel='dns-prefetch'/>
    <link href='https://blogger.googleusercontent.com' rel='preconnect'/>
    <link href='https://fonts.googleapis.com' rel='preconnect'/>
    <link href='https://cdn.pixabay.com' rel='preconnect'/>

    <b:include data='blog' name='all-head-content'/>

    <!-- Structured Data JSON-LD (Schema.org) untuk Rich Snippets Google -->
    <script type='application/ld+json'>
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "WebSite",
          "@id": "<data:blog.canonicalHomepageUrl/>#website",
          "url": "<data:blog.canonicalHomepageUrl/>",
          "name": "<data:blog.title.escaped/>",
          "description": "Portofolio interaktif, aplikasi downloader, dan artikel teknologi oleh Gandzar Subagja",
          "publisher": {
            "@type": "Person",
            "name": "Gandzar Subagja",
            "email": "gandzar@gmail.com",
            "jobTitle": "Fullstack Developer &amp; Hardware Specialist"
          }
        },
        {
          "@type": "Person",
          "@id": "<data:blog.canonicalHomepageUrl/>#author",
          "name": "Gandzar Subagja",
          "url": "<data:blog.canonicalHomepageUrl/>",
          "image": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQr_6Q2B6xIcyzYVfd3D5QpeH0YVaPzGM01Wgsp7msgcZ7X-dKoIdhdOFpO0gWdSxdaZhU-Tzzy_GyA39GF6svcSW9UK-1E39kZMqMjoNizs-Nv65xy_aY6vaFNh4MNiw5q5XphZbilf5uH6DUxQ0oMaGLMDtMK1E34r1GW5FCGVM0hskGWexFUDSZ7RA/s800/icon_untukdi_aboutthisapp.webp",
          "sameAs": [
            "https://github.com",
            "https://instagram.com",
            "https://tiktok.com",
            "https://youtube.com"
          ]
        }
      ]
    }
    </script>

    <!-- Google Analytics (GA4) -->
    <script async='async' src='https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX'></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-XXXXXXXXXX');
    </script>

    <!-- FontAwesome 6.4.0 untuk Koleksi Ikon Lengkap -->
    <link href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css' rel='stylesheet'/>

    <b:skin><![CDATA[
        :root {
            --bg-color: #080b11;
            --card-bg: rgba(17, 24, 39, 0.78);
            --card-bg-elevated: rgba(30, 41, 59, 0.85);
            --text-main: #ffffff;
            --text-sub: #94a3b8;
            --accent-color: #38bdf8;
            --accent-gradient: linear-gradient(135deg, #3b82f6, #06b6d4);
            --accent-glow: rgba(56, 189, 248, 0.35);
            --story-gradient: linear-gradient(45deg, #f09433, #e6683c, #dc2743, #cc2366, #bc1888);
            --border-color: rgba(255, 255, 255, 0.08);
            --border-highlight: rgba(56, 189, 248, 0.3);
            --base-font-size: 16px;
            --main-font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
            --glass-blur: 12px;
            --custom-bg-image: none;
            --radius-sm: 8px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-full: 9999px;
            --transition-smooth: all 0.3s cubic-bezier(0.25, 1, 0.5, 1);
        }

        /* === PRESET THEMES === */
        body.theme-sakura {
            --bg-color: #1a0f18;
            --card-bg: rgba(42, 22, 37, 0.8);
            --card-bg-elevated: rgba(60, 28, 52, 0.9);
            --text-main: #fce7f3;
            --text-sub: #f472b6;
            --accent-color: #ec4899;
            --accent-gradient: linear-gradient(135deg, #ec4899, #f43f5e);
            --accent-glow: rgba(236, 72, 153, 0.35);
            --border-color: rgba(236, 72, 153, 0.15);
            --border-highlight: rgba(236, 72, 153, 0.4);
        }

        body.theme-cyberpunk {
            --bg-color: #09090e;
            --card-bg: rgba(22, 22, 37, 0.85);
            --card-bg-elevated: rgba(35, 30, 58, 0.95);
            --text-main: #00ffcc;
            --text-sub: #ff0055;
            --accent-color: #ff0055;
            --accent-gradient: linear-gradient(135deg, #ff0055, #00ffcc);
            --accent-glow: rgba(255, 0, 85, 0.4);
            --border-color: rgba(0, 255, 204, 0.2);
            --border-highlight: rgba(0, 255, 204, 0.5);
        }

        body.theme-emerald {
            --bg-color: #061512;
            --card-bg: rgba(12, 39, 34, 0.8);
            --card-bg-elevated: rgba(18, 54, 46, 0.9);
            --text-main: #ecfdf5;
            --text-sub: #6ee7b7;
            --accent-color: #10b981;
            --accent-gradient: linear-gradient(135deg, #10b981, #059669);
            --accent-glow: rgba(16, 185, 129, 0.35);
            --border-color: rgba(16, 185, 129, 0.15);
            --border-highlight: rgba(16, 185, 129, 0.4);
        }

        body.theme-sunset {
            --bg-color: #180e0a;
            --card-bg: rgba(41, 24, 17, 0.8);
            --card-bg-elevated: rgba(60, 32, 20, 0.9);
            --text-main: #ffedd5;
            --text-sub: #fdba74;
            --accent-color: #f97316;
            --accent-gradient: linear-gradient(135deg, #f97316, #eab308);
            --accent-glow: rgba(249, 115, 22, 0.35);
            --border-color: rgba(249, 115, 22, 0.15);
            --border-highlight: rgba(249, 115, 22, 0.4);
        }

        body.light-mode {
            --bg-color: #f7f4ed;
            --card-bg: rgba(255, 255, 255, 0.88);
            --card-bg-elevated: rgba(255, 255, 255, 0.98);
            --text-main: #0f172a;
            --text-sub: #64748b;
            --accent-color: #0284c7;
            --accent-gradient: linear-gradient(135deg, #0284c7, #06b6d4);
            --accent-glow: rgba(2, 132, 199, 0.25);
            --border-color: rgba(0, 0, 0, 0.08);
            --border-highlight: rgba(2, 132, 199, 0.3);
        }

        /* === GLOBAL RESET & TYPOGRAPHY === */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: var(--main-font-family);
            -webkit-tap-highlight-color: transparent;
        }

        html {
            scroll-behavior: smooth;
            font-size: var(--base-font-size);
            width: 100%;
        }

        body {
            background-color: var(--bg-color);
            background-image: var(--custom-bg-image);
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: var(--text-main);
            min-height: 100vh;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow-x: hidden;
            position: relative;
            transition: background 0.3s ease, color 0.3s ease;
            line-height: 1.5;
        }

        /* === HEADER === */
        header {
            width: 100%;
            max-width: 520px;
            padding: 14px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--bg-color);
            backdrop-filter: blur(var(--glass-blur));
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid var(--border-color);
            transition: var(--transition-smooth);
        }

        .logo {
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--text-main);
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
        }

        .logo span {
            color: var(--accent-color);
            text-shadow: 0 0 12px var(--accent-glow);
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .header-pill-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-full);
            padding: 6px 12px;
            color: var(--text-main);
            font-size: 0.75rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: var(--transition-smooth);
        }

        .header-pill-btn:hover {
            border-color: var(--accent-color);
            background: rgba(56, 189, 248, 0.1);
        }

        .menu-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            width: 40px;
            height: 40px;
            color: var(--text-main);
            font-size: 1.1rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.2s ease, border-color 0.2s ease;
        }

        .menu-btn:hover { border-color: var(--accent-color); }
        .menu-btn:active { transform: scale(0.9); }

        /* === MEGA DROPDOWN MENU === */
        .dropdown-menu {
            position: absolute;
            top: 65px;
            right: 20px;
            width: 300px;
            max-height: 82vh;
            overflow-y: auto;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 14px;
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
            display: flex;
            flex-direction: column;
            gap: 6px;
            opacity: 0;
            visibility: hidden;
            transform-origin: top right;
            transform: translateY(-15px) scale(0.9);
            transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55), visibility 0.3s ease;
            z-index: 200;
        }

        .dropdown-menu::-webkit-scrollbar { width: 4px; }
        .dropdown-menu::-webkit-scrollbar-thumb { background: var(--border-color); border-radius: 4px; }

        .dropdown-menu.active {
            opacity: 1;
            visibility: visible;
            transform: translateY(0) scale(1);
        }

        .dropdown-menu.closing {
            opacity: 0;
            visibility: hidden;
            transform: translateY(-15px) scale(0.9);
        }

        .dropdown-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 9px 12px;
            color: var(--text-main);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            border-radius: var(--radius-sm);
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid transparent;
            cursor: pointer;
            text-align: left;
            transition: background 0.2s ease, border-color 0.2s ease;
            width: 100%;
        }

        .dropdown-item:hover {
            background: rgba(56, 189, 248, 0.15);
            border-color: var(--border-highlight);
        }

        .dropdown-item-left {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .dropdown-item i {
            color: var(--accent-color);
            font-size: 0.95rem;
            width: 18px;
            text-align: center;
        }

        .menu-divider {
            height: 1px;
            background: var(--border-color);
            margin: 6px 0;
        }

        .menu-title {
            font-size: 0.7rem;
            color: var(--text-sub);
            text-transform: uppercase;
            letter-spacing: 0.6px;
            margin: 4px 0 2px 4px;
            font-weight: 700;
        }

        .preset-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 6px;
            margin-top: 4px;
        }

        .preset-btn {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 6px 10px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
            background: rgba(255, 255, 255, 0.03);
            color: var(--text-main);
            font-size: 0.75rem;
            font-weight: 600;
            cursor: pointer;
            transition: var(--transition-smooth);
        }

        .preset-btn:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: var(--accent-color);
        }

        .preset-badge {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
        }

        .btn-group-sm {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
        }

        .btn-sm {
            padding: 5px 9px;
            font-size: 0.72rem;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-main);
            cursor: pointer;
            transition: var(--transition-smooth);
        }

        .btn-sm:hover, .btn-sm.active {
            background: var(--accent-color);
            color: #fff;
            border-color: var(--accent-color);
        }

        .custom-input-sm {
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 6px 10px;
            color: var(--text-main);
            font-size: 0.78rem;
            outline: none;
        }

        .custom-input-sm:focus {
            border-color: var(--accent-color);
        }

        /* === CONTAINER === */
        .container {
            width: 100%;
            max-width: 520px;
            padding: 24px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* === PROFILE & STORIES AVATAR SECTION === */
        .profile-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-bottom: 28px;
            width: 100%;
        }

        .avatar-container {
            position: relative;
            width: 136px;
            height: 136px;
            margin-bottom: 18px;
        }

        .avatar-wrapper {
            position: relative;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            padding: 4px;
            background: var(--story-gradient);
            box-shadow: 0 0 25px rgba(220, 39, 67, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .avatar-wrapper:hover {
            transform: scale(1.03);
            box-shadow: 0 0 35px rgba(220, 39, 67, 0.5);
        }

        .avatar-wrapper:active {
            transform: scale(0.96);
        }

        .avatar-img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
            display: block !important;
            background-color: #0f172a;
            border: 3px solid var(--bg-color);
        }

        .story-add-badge {
            position: absolute;
            bottom: 3px;
            right: 3px;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: var(--accent-gradient);
            color: #fff;
            border: 3px solid var(--bg-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95rem;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            transition: transform 0.2s ease;
        }

        .story-add-badge:hover {
            transform: scale(1.15) rotate(90deg);
        }

        .profile-title {
            font-size: 1.55rem;
            font-weight: 800;
            line-height: 1.3;
            margin-bottom: 6px;
        }

        .profile-title .highlight {
            color: var(--accent-color);
            text-shadow: 0 0 15px var(--accent-glow);
        }

        .typing-text-container {
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text-sub);
            margin-bottom: 12px;
            min-height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .typing-text { color: var(--text-main); }
        .cursor {
            display: inline-block;
            width: 2px;
            height: 1.1em;
            background-color: var(--accent-color);
            margin-left: 3px;
            animation: blink 0.8s infinite;
        }
        @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }

        .profile-bio {
            color: var(--text-sub);
            font-size: 0.88rem;
            margin-bottom: 16px;
            max-width: 380px;
        }

        .email-box {
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-full);
            padding: 8px 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.85rem;
            color: var(--text-sub);
            margin-bottom: 18px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.15);
        }

        .copy-btn {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 4px 9px;
            border-radius: var(--radius-full);
            cursor: pointer;
            transition: var(--transition-smooth);
            font-size: 0.78rem;
        }

        .copy-btn:hover {
            background: var(--accent-color);
            color: #fff;
        }

        .profile-buttons {
            display: flex;
            gap: 10px;
            width: 100%;
            max-width: 360px;
            margin-bottom: 12px;
        }

        .btn-primary {
            flex: 1;
            background: var(--accent-gradient);
            color: #fff;
            padding: 10px 14px;
            border-radius: var(--radius-md);
            font-weight: 700;
            text-decoration: none;
            font-size: 0.88rem;
            text-align: center;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 15px var(--accent-glow);
            transition: var(--transition-smooth);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px var(--accent-glow);
        }

        .btn-secondary {
            flex: 1;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 10px 14px;
            border-radius: var(--radius-md);
            font-weight: 600;
            text-decoration: none;
            font-size: 0.88rem;
            text-align: center;
            cursor: pointer;
            transition: var(--transition-smooth);
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
        }

        .btn-secondary:hover {
            border-color: var(--accent-color);
            background: rgba(56, 189, 248, 0.08);
        }

        /* === VIEW MODE SWITCHER TABS === */
        .view-switcher-bar {
            width: 100%;
            display: flex;
            gap: 6px;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            padding: 6px;
            border-radius: var(--radius-lg);
            margin-bottom: 24px;
            overflow-x: auto;
        }

        .view-switcher-bar::-webkit-scrollbar { display: none; }

        .view-tab-btn {
            flex: 1;
            white-space: nowrap;
            padding: 8px 12px;
            border-radius: 12px;
            border: none;
            background: transparent;
            color: var(--text-sub);
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: var(--transition-smooth);
        }

        .view-tab-btn.active {
            background: var(--accent-gradient);
            color: #fff;
            box-shadow: 0 4px 12px var(--accent-glow);
        }

        .view-tab-btn:hover:not(.active) {
            color: var(--text-main);
            background: rgba(255, 255, 255, 0.05);
        }

        /* === SECTIONS COMMONS === */
        .section-box {
            width: 100%;
            margin-bottom: 35px;
        }

        .section-header-box {
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            margin-bottom: 14px;
        }

        .section-title {
            font-size: 1.25rem;
            font-weight: 800;
            letter-spacing: -0.3px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .section-sub {
            color: var(--text-sub);
            font-size: 0.8rem;
            margin-top: 2px;
        }

        /* ========================================================
           SECTION 1: 3D COVERFLOW BLOG SLIDER
           ======================================================== */
        .slider-section-container {
            position: relative;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .slider-viewport {
            width: 100%;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 330px;
            perspective: 1000px;
        }

        .slider-track {
            display: flex;
            width: 100%;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        .slide-card-item {
            position: absolute;
            width: 255px;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            transition: all 0.45s cubic-bezier(0.25, 1, 0.5, 1);
            opacity: 0;
            pointer-events: none;
            transform: scale(0.8) translateX(0);
            cursor: pointer;
        }

        .slide-card-item.active {
            opacity: 1;
            pointer-events: auto;
            z-index: 10;
            transform: scale(1) translateX(0);
            box-shadow: 0 16px 36px rgba(0,0,0,0.4), 0 0 20px var(--accent-glow);
            border-color: var(--border-highlight);
        }

        .slide-card-item.prev {
            opacity: 0.45;
            z-index: 5;
            transform: scale(0.85) translateX(-145px);
        }

        .slide-card-item.next {
            opacity: 0.45;
            z-index: 5;
            transform: scale(0.85) translateX(145px);
        }

        .card-new-badge {
            position: absolute;
            top: 12px;
            right: 12px;
            background: #ef4444;
            color: #fff;
            font-size: 0.65rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: var(--radius-full);
            letter-spacing: 0.5px;
            box-shadow: 0 0 10px rgba(239, 68, 68, 0.6);
            z-index: 2;
        }

        .slide-card-thumb {
            width: 100%;
            height: 120px;
            border-radius: 12px;
            object-fit: cover;
            margin-bottom: 12px;
            background-color: var(--card-bg-elevated);
        }

        .slide-card-title {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 6px;
            line-height: 1.35;
            color: var(--accent-color);
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .slide-card-snippet {
            font-size: 0.78rem;
            color: var(--text-sub);
            line-height: 1.4;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            margin-bottom: 12px;
        }

        .card-like-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 10px;
            padding-top: 8px;
            border-top: 1px solid var(--border-color);
            gap: 6px;
        }

        .like-btn, .follow-btn {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            color: var(--text-sub);
            padding: 5px 11px;
            border-radius: var(--radius-full);
            font-size: 0.72rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            transition: var(--transition-smooth);
        }

        .like-btn:hover { color: #ef4444; border-color: rgba(239, 68, 68, 0.4); }
        .like-btn.liked {
            color: #ef4444;
            border-color: rgba(239, 68, 68, 0.5);
            background: rgba(239, 68, 68, 0.12);
        }

        .follow-btn:hover { color: #10b981; border-color: rgba(16, 185, 129, 0.4); }
        .follow-btn.following {
            color: #10b981;
            border-color: rgba(16, 185, 129, 0.5);
            background: rgba(16, 185, 129, 0.12);
        }

        .slider-arrow-btn {
            position: absolute;
            top: 48%;
            transform: translateY(-50%);
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            color: var(--text-main);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 20;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            transition: var(--transition-smooth);
        }

        .slider-arrow-btn:hover {
            background: var(--accent-color);
            color: #fff;
            transform: translateY(-50%) scale(1.1);
        }

        .slider-arrow-btn.prev-arrow { left: -6px; }
        .slider-arrow-btn.next-arrow { right: -6px; }

        .slider-footer-controls {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            margin-top: 18px;
            width: 100%;
        }

        .slide-counter-badge {
            background: rgba(56, 189, 248, 0.12);
            color: var(--accent-color);
            border: 1px solid var(--border-highlight);
            padding: 4px 14px;
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 1px;
        }

        .slide-dots-wrapper { display: flex; gap: 6px; align-items: center; }
        .slide-dot-item {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--text-sub);
            opacity: 0.35;
            cursor: pointer;
            transition: 0.3s;
        }

        .slide-dot-item.active {
            opacity: 1;
            background: var(--accent-color);
            width: 22px;
            border-radius: 10px;
            box-shadow: 0 0 10px var(--accent-glow);
        }

        .download-apk-btn {
            background: var(--accent-gradient);
            color: #fff;
            border: none;
            padding: 10px 22px;
            border-radius: var(--radius-full);
            font-size: 0.85rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            margin-top: 6px;
            box-shadow: 0 6px 18px var(--accent-glow);
            text-decoration: none;
            transition: var(--transition-smooth);
        }

        .download-apk-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 24px var(--accent-glow);
        }

        /* ========================================================
           SECTION 2: MARKETPLACE HORIZONTAL CAROUSEL
           ======================================================== */
        .marketplace-slider-wrapper {
            position: relative;
            width: 100%;
            margin: 0 -20px;
            padding: 0 20px;
            width: calc(100% + 40px);
        }

        .marketplace-track {
            display: flex;
            gap: 14px;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            scroll-behavior: smooth;
            padding: 6px 4px 16px 4px;
            -webkit-overflow-scrolling: touch;
        }

        .marketplace-track::-webkit-scrollbar { display: none; }
        .marketplace-track { -ms-overflow-style: none; scrollbar-width: none; }

        .market-card {
            flex: 0 0 180px;
            scroll-snap-align: start;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 11px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            box-shadow: 0 8px 22px rgba(0,0,0,0.25);
            transition: var(--transition-smooth);
            cursor: pointer;
        }

        .market-card:hover, .market-card:active {
            transform: translateY(-5px);
            border-color: var(--accent-color);
            box-shadow: 0 14px 28px rgba(0,0,0,0.35), 0 0 15px var(--accent-glow);
        }

        .market-card-thumb-box {
            position: relative;
            width: 100%;
            height: 125px;
            border-radius: 10px;
            overflow: hidden;
            background-color: var(--card-bg-elevated);
            margin-bottom: 10px;
        }

        .market-card-thumb {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.35s ease;
        }

        .market-card:hover .market-card-thumb { transform: scale(1.08); }

        .card-badge-tag {
            position: absolute;
            top: 6px;
            left: 6px;
            background: var(--accent-gradient);
            color: #fff;
            font-size: 0.6rem;
            font-weight: 800;
            padding: 3px 8px;
            border-radius: 6px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.4);
            letter-spacing: 0.4px;
            z-index: 2;
        }

        .market-card-content {
            display: flex;
            flex-direction: column;
            gap: 4px;
            flex-grow: 1;
        }

        .market-card-title {
            font-size: 0.85rem;
            font-weight: 700;
            color: var(--text-main);
            line-height: 1.35;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            min-height: 2.7em;
        }

        .market-card-desc {
            font-size: 0.72rem;
            color: var(--text-sub);
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            line-height: 1.3;
            margin-bottom: 8px;
        }

        .market-card-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 8px;
            border-top: 1px dashed var(--border-color);
            margin-top: auto;
        }

        .slider-scroll-nav {
            display: flex;
            gap: 6px;
        }

        .scroll-nav-btn {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.75rem;
            transition: var(--transition-smooth);
        }

        .scroll-nav-btn:hover {
            background: var(--accent-color);
            color: #fff;
            border-color: var(--accent-color);
        }

        /* ========================================================
           SECTION 3: 4-COLUMN PHOTO & APP GALLERY GRID
           ======================================================== */
        .search-box-container {
            position: relative;
            width: 100%;
            margin-top: 8px;
            margin-bottom: 12px;
        }

        .search-input {
            width: 100%;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 10px 38px 10px 40px;
            color: var(--text-main);
            font-size: 0.85rem;
            outline: none;
            transition: var(--transition-smooth);
        }

        .search-input:focus {
            border-color: var(--accent-color);
            box-shadow: 0 0 16px var(--accent-glow);
        }

        .search-icon-inside {
            position: absolute;
            left: 14px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-sub);
            font-size: 0.9rem;
        }

        .search-clear-btn {
            position: absolute;
            right: 12px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: var(--text-sub);
            cursor: pointer;
            font-size: 0.85rem;
            display: none;
        }

        .filter-tags-scroll {
            display: flex;
            gap: 6px;
            overflow-x: auto;
            margin-bottom: 14px;
            padding-bottom: 4px;
        }

        .filter-tags-scroll::-webkit-scrollbar { display: none; }

        .filter-tag-pill {
            padding: 5px 12px;
            border-radius: var(--radius-full);
            border: 1px solid var(--border-color);
            background: rgba(255, 255, 255, 0.04);
            color: var(--text-sub);
            font-size: 0.73rem;
            font-weight: 600;
            cursor: pointer;
            white-space: nowrap;
            transition: var(--transition-smooth);
        }

        .filter-tag-pill.active, .filter-tag-pill:hover {
            background: var(--accent-gradient);
            color: #fff;
            border-color: transparent;
            box-shadow: 0 2px 8px var(--accent-glow);
        }

        .gallery-grid-container {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 7px;
            width: 100%;
        }

        .gallery-card {
            position: relative;
            width: 100%;
            aspect-ratio: 1 / 1;
            border-radius: 12px;
            overflow: hidden;
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            cursor: pointer;
            transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
        }

        .gallery-card:hover, .gallery-card:active {
            transform: scale(0.97);
            border-color: var(--accent-color);
            box-shadow: 0 0 15px var(--accent-glow);
            z-index: 2;
        }

        .gallery-thumb {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            background-color: var(--card-bg-elevated);
        }

        .gallery-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.2) 60%, transparent 100%);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 6px;
            opacity: 0;
            transition: opacity 0.25s ease;
        }

        .gallery-card:hover .gallery-overlay, .gallery-card:active .gallery-overlay {
            opacity: 1;
        }

        .gallery-title {
            font-size: 0.65rem;
            font-weight: 700;
            color: #fff;
            line-height: 1.25;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        .gallery-badge {
            position: absolute;
            top: 4px;
            right: 4px;
            background: rgba(0, 0, 0, 0.65);
            backdrop-filter: blur(4px);
            color: #fff;
            font-size: 0.55rem;
            font-weight: 700;
            padding: 2px 5px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            gap: 3px;
            z-index: 2;
        }

        /* ========================================================
           SECTION 4: LINKS & SOCIALS HUB (GLOWING ANIMATED CARDS)
           ======================================================== */
        .links-list {
            width: 100%;
            display: flex;
            flex-direction: column;
            gap: 14px;
            margin-top: 15px;
        }

        .link-card {
            position: relative;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            text-decoration: none;
            color: var(--text-main);
            overflow: hidden;
            z-index: 1;
            transition: transform 0.25s ease;
        }

        .link-card:hover {
            transform: translateY(-2px);
        }

        .link-card::before {
            content: '';
            position: absolute;
            width: 120px;
            height: 120px;
            background: radial-gradient(circle, var(--accent-color) 0%, #2563eb 50%, transparent 70%);
            border-radius: 50%;
            filter: blur(4px);
            offset-path: rect(0% 100% 100% 0% round 14px);
            animation: moveAlongBorder 6s ease-in-out infinite alternate;
            z-index: -1;
            pointer-events: none;
        }

        .link-card::after {
            content: '';
            position: absolute;
            inset: 1.5px;
            background: var(--card-bg);
            border-radius: 12.5px;
            z-index: -1;
        }

        @keyframes moveAlongBorder {
            0% { offset-distance: 50%; }
            100% { offset-distance: 100%; }
        }

        .card-left { display: flex; align-items: center; gap: 14px; }
        .icon-box {
            width: 42px;
            height: 42px;
            border-radius: 12px;
            background: rgba(59, 130, 246, 0.15);
            color: var(--accent-color);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.15rem;
        }

        .card-info h3 { font-size: 0.94rem; font-weight: 700; margin-bottom: 2px; }
        .card-info p { font-size: 0.75rem; color: var(--text-sub); }
        .arrow-icon { color: var(--text-sub); font-size: 0.9rem; transition: transform 0.2s ease; }
        .link-card:hover .arrow-icon { transform: translateX(3px); color: var(--accent-color); }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 15px;
            flex-wrap: wrap;
        }

        .social-icon {
            width: 40px;
            height: 40px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-sub);
            text-decoration: none;
            transition: var(--transition-smooth);
            font-size: 1.1rem;
        }

        .social-icon:hover {
            background: var(--accent-color);
            color: #fff;
            transform: translateY(-3px);
            box-shadow: 0 4px 12px var(--accent-glow);
        }

        /* ========================================================
           SECTION 5: BLOG TRAFFIC & LIVE STATS
           ======================================================== */
        .traffic-card {
            width: 100%;
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 20px;
            margin-bottom: 35px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .badge-live {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            color: var(--accent-color);
            font-size: 0.8rem;
            font-weight: 700;
            margin-bottom: 14px;
        }

        .live-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: #10b981;
            box-shadow: 0 0 10px #10b981;
            animation: pulseDot 1.5s infinite;
        }

        @keyframes pulseDot {
            0% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.4); opacity: 0.6; }
            100% { transform: scale(1); opacity: 1; }
        }

        .stat-grid-top {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            text-align: center;
            margin-bottom: 16px;
            padding-bottom: 14px;
            border-bottom: 1px solid var(--border-color);
        }

        .stat-box-item .num {
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--accent-color);
            letter-spacing: -0.5px;
        }

        .stat-box-item .lbl { font-size: 0.72rem; color: var(--text-sub); margin-top: 2px; }
        .stat-list-detail { display: flex; flex-direction: column; gap: 8px; }
        .stat-row { display: flex; justify-content: space-between; align-items: center; font-size: 0.82rem; color: var(--text-sub); }
        .stat-row span.val { font-weight: 700; color: var(--text-main); }

        /* === FOOTER === */
        footer {
            text-align: center;
            font-size: 0.78rem;
            color: var(--text-sub);
            padding-bottom: 35px;
            line-height: 1.6;
        }

        /* ========================================================
           FULLSCREEN STORY VIEWER MODAL
           ======================================================== */
        .story-modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0, 0, 0, 0.96);
            backdrop-filter: blur(20px);
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease;
        }

        .story-modal-overlay.active { opacity: 1; visibility: visible; }

        .story-card-box {
            position: relative;
            width: 100%;
            max-width: 410px;
            height: 90vh;
            max-height: 740px;
            background: #000;
            border-radius: var(--radius-lg);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8);
        }

        .story-progress-container {
            position: absolute;
            top: 12px; left: 12px; right: 12px;
            display: flex;
            gap: 4px;
            z-index: 20;
        }

        .story-progress-segment {
            flex: 1;
            height: 3px;
            background: rgba(255, 255, 255, 0.35);
            border-radius: 3px;
            overflow: hidden;
        }

        .story-progress-fill { height: 100%; width: 0%; background: #fff; }

        .story-header {
            position: absolute;
            top: 22px; left: 12px; right: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            z-index: 20;
        }

        .story-user-info { display: flex; align-items: center; gap: 10px; }
        .story-user-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid var(--accent-color);
        }

        .story-username { font-size: 0.88rem; font-weight: 700; color: #fff; }
        .story-time {
            font-size: 0.72rem;
            color: rgba(255, 255, 255, 0.85);
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .story-controls-top { display: flex; align-items: center; gap: 12px; }
        .story-action-btn {
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            width: 34px;
            height: 34px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.95rem;
            cursor: pointer;
            transition: var(--transition-smooth);
        }

        .story-action-btn:hover { background: rgba(255, 255, 255, 0.2); }
        .story-action-btn.delete-btn { color: #ef4444; }

        .story-media-wrapper {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            background: #000;
        }

        .story-media-wrapper img, .story-media-wrapper video {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .story-nav-touch {
            position: absolute;
            top: 60px;
            bottom: 60px;
            width: 35%;
            z-index: 10;
        }

        .story-nav-left { left: 0; }
        .story-nav-right { right: 0; }

        .story-caption-box {
            position: absolute;
            bottom: 20px; left: 16px; right: 16px;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            padding: 10px 14px;
            border-radius: 12px;
            color: #fff;
            font-size: 0.82rem;
            text-align: center;
            z-index: 20;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* ========================================================
           UPLOAD STORY MODAL (INDEXEDDB UP TO 100MB+)
           ======================================================== */
        .upload-modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(8, 11, 17, 0.88);
            backdrop-filter: blur(10px);
            z-index: 1500;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease;
        }

        .upload-modal-overlay.active { opacity: 1; visibility: visible; }

        .upload-modal-box {
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 420px;
            padding: 22px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            position: relative;
            box-shadow: 0 20px 50px rgba(0,0,0,0.6);
        }

        .upload-title {
            font-size: 1.15rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .upload-field { display: flex; flex-direction: column; gap: 6px; }
        .upload-field label { font-size: 0.78rem; color: var(--text-sub); font-weight: 600; }
        .upload-field input, .upload-field textarea {
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 9px 12px;
            color: var(--text-main);
            font-size: 0.82rem;
            outline: none;
        }

        .upload-field input:focus, .upload-field textarea:focus { border-color: var(--accent-color); }
        .loading-status { display: none; font-size: 0.8rem; color: var(--accent-color); text-align: center; }

        /* ========================================================
           POST READING & INTERACTIVE COMMENT MODAL
           ======================================================== */
        .post-modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(8, 11, 17, 0.88);
            backdrop-filter: blur(10px);
            z-index: 1000;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s ease, visibility 0.3s ease;
        }

        .post-modal-overlay.active { opacity: 1; visibility: visible; }

        .post-modal-container {
            background: var(--card-bg);
            backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            width: 100%;
            max-width: 500px;
            max-height: 88vh;
            overflow-y: auto;
            padding: 24px;
            position: relative;
            box-shadow: 0 25px 50px rgba(0,0,0,0.7);
            transform: scale(0.88);
            transition: transform 0.35s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }

        .post-modal-overlay.active .post-modal-container { transform: scale(1); }

        .post-modal-close {
            position: absolute;
            top: 16px; right: 16px;
            width: 34px; height: 34px;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            font-size: 1rem;
            cursor: pointer;
            display: flex; align-items: center; justify-content: center;
            transition: var(--transition-smooth);
        }

        .post-modal-close:hover { background: #ef4444; color: #fff; }

        .post-modal-header {
            margin-bottom: 14px;
            padding-right: 36px;
        }

        .post-meta-bar {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 0.75rem;
            color: var(--text-sub);
            margin-bottom: 6px;
            flex-wrap: wrap;
        }

        .post-meta-item { display: inline-flex; align-items: center; gap: 4px; }

        .post-modal-title {
            font-size: 1.3rem;
            font-weight: 800;
            color: var(--text-main);
            line-height: 1.35;
        }

        /* Toolbar Reader: TTS Voice, Font Zoom, Share */
        .reader-toolbar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 6px 12px;
            margin-bottom: 16px;
            gap: 8px;
            flex-wrap: wrap;
        }

        .tts-btn {
            background: transparent;
            border: none;
            color: var(--accent-color);
            font-size: 0.78rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
        }

        .font-zoom-group {
            display: flex;
            gap: 4px;
            align-items: center;
        }

        .font-zoom-btn {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            width: 26px;
            height: 26px;
            border-radius: 6px;
            font-size: 0.72rem;
            font-weight: 700;
            cursor: pointer;
        }

        .post-modal-body {
            font-size: 0.9rem;
            color: var(--text-main);
            line-height: 1.7;
            word-break: break-word;
        }

        .post-modal-body img {
            max-width: 100%;
            height: auto;
            border-radius: 12px;
            margin: 12px 0;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }

        .post-modal-body p { margin-bottom: 12px; }

        .modal-action-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px dashed var(--border-color);
            gap: 8px;
            flex-wrap: wrap;
        }

        .action-btn-group { display: flex; gap: 8px; align-items: center; }

        .share-love-btn {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 6px 14px;
            border-radius: var(--radius-full);
            font-size: 0.75rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
            transition: var(--transition-smooth);
        }

        .share-love-btn:hover {
            background: rgba(56, 189, 248, 0.15);
            border-color: var(--accent-color);
        }

        /* Modern Comment Box */
        .comments-section {
            margin-top: 20px;
            padding-top: 18px;
            border-top: 1px solid var(--border-color);
        }

        .comments-title {
            font-size: 1rem;
            font-weight: 800;
            margin-bottom: 14px;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .comment-input-box {
            display: flex;
            flex-direction: column;
            gap: 8px;
            margin-bottom: 16px;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-color);
            padding: 12px;
            border-radius: var(--radius-md);
        }

        .comment-input-box input, .comment-input-box textarea {
            width: 100%;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 9px 12px;
            color: var(--text-main);
            font-size: 0.82rem;
            outline: none;
            transition: border-color 0.2s ease;
        }

        .comment-input-box input:focus, .comment-input-box textarea:focus {
            border-color: var(--accent-color);
        }

        .comment-input-box textarea { resize: vertical; min-height: 65px; }

        .comment-form-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .cancel-edit-btn {
            background: transparent;
            border: none;
            color: #ef4444;
            font-size: 0.78rem;
            cursor: pointer;
            display: none;
        }

        .comment-submit-btn {
            background: var(--accent-gradient);
            color: #fff;
            border: none;
            padding: 7px 16px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.8rem;
            cursor: pointer;
            box-shadow: 0 4px 12px var(--accent-glow);
            transition: var(--transition-smooth);
        }

        .comment-submit-btn:hover {
            transform: translateY(-1px);
        }

        .comments-list {
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-height: 250px;
            overflow-y: auto;
        }

        .comment-item {
            background: rgba(255, 255, 255, 0.025);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 11px 13px;
            font-size: 0.82rem;
            position: relative;
        }

        .comment-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 5px;
        }

        .comment-author-box {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .comment-avatar-initials {
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: var(--accent-gradient);
            color: #fff;
            font-size: 0.65rem;
            font-weight: 800;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .comment-author { font-weight: 700; color: var(--accent-color); font-size: 0.85rem; }
        .comment-actions { display: flex; gap: 8px; }

        .comment-action-btn {
            background: transparent;
            border: none;
            color: var(--text-sub);
            font-size: 0.75rem;
            cursor: pointer;
            transition: color 0.2s ease;
        }

        .comment-action-btn:hover { color: var(--text-main); }
        .comment-action-btn.delete:hover { color: #ef4444; }

        .comment-text { color: var(--text-main); line-height: 1.45; word-break: break-word; }
        .comment-time { font-size: 0.7rem; color: var(--text-sub); margin-top: 4px; }

        /* ========================================================
           RECENT COMMENTS MODAL DIALOG
           ======================================================== */
        .recent-dialog-item {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            gap: 6px;
            text-align: left;
            cursor: pointer;
            transition: border-color 0.2s ease, transform 0.2s ease;
        }

        .recent-dialog-item:hover {
            border-color: var(--accent-color);
            transform: translateY(-2px);
            background: rgba(56, 189, 248, 0.08);
        }

        .recent-dialog-author {
            font-weight: 700;
            font-size: 0.82rem;
            color: var(--accent-color);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .recent-dialog-text {
            font-size: 0.83rem;
            color: var(--text-main);
            line-height: 1.4;
            word-break: break-word;
        }

        .recent-dialog-post {
            font-size: 0.74rem;
            color: var(--text-sub);
            display: inline-flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
            margin-top: 2px;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
        }

        .recent-dialog-post:hover { color: var(--accent-color); }

        /* ========================================================
           404 ERROR PAGE STYLES
           ======================================================== */
        .error-404-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 75vh;
            text-align: center;
            padding: 20px;
            width: 100%;
            max-width: 480px;
        }

        .error-code {
            font-size: 6rem;
            font-weight: 900;
            line-height: 1;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 30px var(--accent-glow);
            margin-bottom: 10px;
            animation: pulseGlow 2s infinite alternate;
        }

        @keyframes pulseGlow {
            0% { transform: scale(1); filter: drop-shadow(0 0 10px var(--accent-color)); }
            100% { transform: scale(1.05); filter: drop-shadow(0 0 25px var(--accent-color)); }
        }

        .error-icon-box {
            font-size: 3rem;
            color: var(--accent-color);
            margin-bottom: 15px;
        }

        .error-title {
            font-size: 1.5rem;
            font-weight: 800;
            margin-bottom: 8px;
            color: var(--text-main);
        }

        .error-desc {
            font-size: 0.88rem;
            color: var(--text-sub);
            margin-bottom: 25px;
            line-height: 1.5;
        }

        .error-btn-home {
            background: var(--accent-gradient);
            color: #fff;
            padding: 12px 28px;
            border-radius: var(--radius-md);
            font-weight: 700;
            text-decoration: none;
            font-size: 0.9rem;
            box-shadow: 0 10px 20px rgba(0,0,0,0.3);
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: transform 0.2s ease;
        }

        .error-btn-home:active { transform: scale(0.95); }

        .error-timer {
            margin-top: 15px;
            font-size: 0.78rem;
            color: var(--text-sub);
        }

        /* ========================================================
           TOUCH RIPPLE, PARTICLES & TOAST NOTIFICATION
           ======================================================== */
        .touch-container {
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 9999;
        }

        .touch-ring {
            position: absolute;
            width: 32px; height: 32px;
            border: 2px solid var(--accent-color);
            border-radius: 50%;
            transform: translate(-50%, -50%) scale(0.3);
            opacity: 0;
            animation: ringExpand 0.7s ease-out forwards;
        }

        @keyframes ringExpand {
            0% { transform: translate(-50%, -50%) scale(0.2); opacity: 0; }
            30% { transform: translate(-50%, -50%) scale(1); opacity: 1; }
            100% { transform: translate(-50%, -50%) scale(2.4); opacity: 0; }
        }

        .falling-particle {
            position: fixed;
            top: -30px;
            pointer-events: none;
            z-index: 99;
            animation: fall linear infinite;
        }

        @keyframes fall {
            to { transform: translateY(105vh) rotate(360deg); }
        }

        .scroll-reveal {
            opacity: 0;
            transform: translateY(35px) scale(0.95);
            transition: transform 0.7s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.6s ease-out;
        }

        .scroll-reveal.revealed {
            opacity: 1;
            transform: translateY(0) scale(1);
        }

        /* Modern Toast */
        .toast-container {
            position: fixed;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 99999;
            display: flex;
            flex-direction: column;
            gap: 8px;
            pointer-events: none;
        }

        .toast-msg {
            background: var(--card-bg-elevated);
            backdrop-filter: blur(12px);
            border: 1px solid var(--border-highlight);
            color: #fff;
            padding: 10px 18px;
            border-radius: var(--radius-full);
            font-size: 0.82rem;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(0,0,0,0.4);
            display: flex;
            align-items: center;
            gap: 8px;
            animation: toastPop 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
        }

        @keyframes toastPop {
            0% { transform: scale(0.8) translateY(10px); opacity: 0; }
            100% { transform: scale(1) translateY(0); opacity: 1; }
        }

        /* Floating Heart on Like */
        .floating-heart {
            position: fixed;
            pointer-events: none;
            color: #ef4444;
            font-size: 1.2rem;
            z-index: 9999;
            animation: floatUp 1.2s ease-out forwards;
        }

        @keyframes floatUp {
            0% { transform: translate(-50%, -50%) scale(0.5); opacity: 1; }
            50% { transform: translate(-50%, -90px) scale(1.3); opacity: 0.8; }
            100% { transform: translate(-50%, -150px) scale(1.6); opacity: 0; }
        }

        .main { display: none !important; }
    ]]></b:skin>
  </head>

  <body>
    <!-- HEADER NAVIGASI -->
    <header>
      <a class='logo' href='/'>
        <span>bagja</span>.dev
      </a>

      <div class='header-actions'>
        <button class='header-pill-btn' onclick='openStoryModal()' title='Lihat Story'>
          <i class='fa-solid fa-circle-play' style='color:#ec4899;'/> Story
        </button>

        <button class='menu-btn' id='menuToggle' onclick='toggleMenu()' title='Buka Menu Pengaturan'>
          <i class='fa-solid fa-ellipsis-vertical' id='menuIcon'/>
        </button>
      </div>

      <!-- MEGA DROPDOWN MENU -->
      <div class='dropdown-menu' id='dropdownMenu'>
        <div class='dropdown-item' style='background:transparent; cursor:default; padding:4px 8px;'>
          <span style='font-size:0.75rem; color:var(--text-sub);'><i class='fa-regular fa-clock'/> <span id='liveClock'>--:--:--</span></span>
        </div>

        <a class='dropdown-item' href='/' onclick='closeMenu()'>
          <span class='dropdown-item-left'><i class='fa-solid fa-house'/> Home / Beranda</span>
        </a>
        <a class='dropdown-item' href='#sliderSection' onclick='closeMenu()'>
          <span class='dropdown-item-left'><i class='fa-regular fa-newspaper'/> 3D Coverflow Slider</span>
        </a>
        <a class='dropdown-item' href='#marketplaceSection' onclick='closeMenu()'>
          <span class='dropdown-item-left'><i class='fa-solid fa-shop'/> Marketplace Apps</span>
        </a>
        <a class='dropdown-item' href='#gallerySection' onclick='closeMenu()'>
          <span class='dropdown-item-left'><i class='fa-solid fa-images'/> Galeri 4-Kolom</span>
        </a>
        <button class='dropdown-item' onclick='openRecentCommentsModal()'>
          <span class='dropdown-item-left'><i class='fa-regular fa-comments'/> Komentar Terbaru</span>
        </button>
        <button class='dropdown-item' onclick='openUploadStoryModal(event)'>
          <span class='dropdown-item-left'><i class='fa-solid fa-camera'/> Tambah Story Baru</span>
        </button>

        <div class='menu-divider'/>
        <div class='menu-title'>Preset Tema Blog</div>
        <div class='preset-grid'>
          <button class='preset-btn' onclick='applyThemePreset("default")'>
            <span class='preset-badge' style='background:#38bdf8;'/> Default Cyan
          </button>
          <button class='preset-btn' onclick='applyThemePreset("sakura")'>
            <span class='preset-badge' style='background:#ec4899;'/> Sakura Pink
          </button>
          <button class='preset-btn' onclick='applyThemePreset("cyberpunk")'>
            <span class='preset-badge' style='background:#ff0055;'/> Cyber Neon
          </button>
          <button class='preset-btn' onclick='applyThemePreset("emerald")'>
            <span class='preset-badge' style='background:#10b981;'/> Emerald Mint
          </button>
          <button class='preset-btn' onclick='applyThemePreset("sunset")'>
            <span class='preset-badge' style='background:#f97316;'/> Sunset Gold
          </button>
          <button class='preset-btn' onclick='toggleThemeMode()'>
            <span class='preset-badge' style='background:#f7f4ed; border:1px solid #ccc;'/> Light Cream
          </button>
        </div>

        <div class='menu-divider'/>
        <div class='menu-title'>Warna &amp; Gambar Latar (Wallpaper)</div>
        <div class='dropdown-item' style='cursor:default; flex-direction:column; align-items:flex-start; gap:8px;'>
          <div style='display:flex; gap:6px; width:100%; align-items:center;'>
            <input id='bgPickerColor' onchange='setCustomBgColor(this.value)' style='width:32px; height:32px; border:none; border-radius:6px; cursor:pointer;' type='color' value='#080b11'/>
            <button class='btn-sm' onclick='setGradientBg("linear-gradient(135deg, #1e3c72 0%, #2a5298 100%)")'>Biru Gradien</button>
            <button class='btn-sm' onclick='setGradientBg("linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%)")'>Cyber</button>
          </div>
          <div style='width:100%; display:flex; gap:4px;'>
            <input id='bgUrlInput' class='custom-input-sm' placeholder='Paste URL Gambar...' type='text'/>
            <button class='btn-sm' onclick='setBgUrlFromInput()'>Set</button>
          </div>
          <div style='width:100%; display:flex; gap:6px; align-items:center;'>
            <label class='btn-sm' style='text-align:center; flex:1; cursor:pointer;' for='bgFileInput'><i class='fa-solid fa-upload'/> Dari Galeri HP</label>
            <input accept='image/*' id='bgFileInput' onchange='handleBgFileUpload(event)' style='display:none;' type='file'/>
            <button class='btn-sm' onclick='resetCustomBg()'>Reset</button>
          </div>
        </div>

        <div class='menu-divider'/>
        <div class='menu-title'>Efek Kaca (Glassmorphism)</div>
        <div class='dropdown-item' style='cursor:default;'>
          <span class='dropdown-item-left'><i class='fa-solid fa-wand-magic-sparkles'/> Blur Latar</span>
          <div class='btn-group-sm'>
            <button class='btn-sm' onclick='setGlassBlur("0px")'>Off</button>
            <button class='btn-sm' onclick='setGlassBlur("12px")'>Sedang</button>
            <button class='btn-sm' onclick='setGlassBlur("25px")'>Tebal</button>
          </div>
        </div>

        <div class='menu-divider'/>
        <div class='menu-title'>Animasi Partikel Jatuh</div>
        <button class='dropdown-item' onclick='toggleBubbles()'>
          <span class='dropdown-item-left'><i class='fa-solid fa-soap'/> Sakelar Efek Jatuh</span>
          <span id='bubbleStatus' style='font-size:0.75rem; color:#10b981; font-weight:bold;'>ON</span>
        </button>
        <div class='btn-group-sm' style='padding:4px 6px;'>
          <button class='btn-sm' onclick='setBgAnimation("leaf")'>🍃 Daun</button>
          <button class='btn-sm' onclick='setBgAnimation("snow")'>❄️ Salju</button>
          <button class='btn-sm' onclick='setBgAnimation("star")'>✨ Bintang</button>
          <button class='btn-sm' onclick='setBgAnimation("heart")'>❤️ Cinta</button>
          <button class='btn-sm' onclick='setBgAnimation("none")'>❌ Matikan</button>
        </div>

        <div class='menu-divider'/>
        <div class='menu-title'>Jenis Font (Font Family)</div>
        <div class='dropdown-item' style='cursor:default; flex-direction:column; align-items:flex-start; gap:6px;'>
          <div class='btn-group-sm' style='width:100%;'>
            <button class='btn-sm' onclick='setFontFamily("sans")'>Sans</button>
            <button class='btn-sm' onclick='setFontFamily("serif")'>Serif</button>
            <button class='btn-sm' onclick='setFontFamily("mono")'>Code</button>
            <button class='btn-sm' onclick='setFontFamily("cursive")'>Comic</button>
          </div>
        </div>

        <div class='menu-divider'/>
        <div class='menu-title'>Ukuran Teks (Font Size)</div>
        <div class='dropdown-item' style='cursor:default;'>
          <span class='dropdown-item-left'><i class='fa-solid fa-font'/> Ukuran Font</span>
          <div class='btn-group-sm'>
            <button class='btn-sm' onclick='setFontSize("14px")'>Small</button>
            <button class='btn-sm' onclick='setFontSize("16px")'>Normal</button>
            <button class='btn-sm' onclick='setFontSize("18px")'>Large</button>
          </div>
        </div>

        <div class='menu-divider'/>
        <div class='menu-title'>Musik Santai (Lo-Fi)</div>
        <button class='dropdown-item' onclick='toggleAmbientAudio()'>
          <span class='dropdown-item-left'><i class='fa-solid fa-music'/> Audio Lofi Relax</span>
          <span id='audioStatus' style='font-size:0.75rem; color:var(--text-sub);'>OFF</span>
        </button>

        <div class='menu-divider'/>
        <div class='menu-title'>Bagikan Blog</div>
        <button class='dropdown-item' onclick='shareProfile()'>
          <span class='dropdown-item-left'><i class='fa-solid fa-share-nodes'/> Share Blog URL</span>
          <i class='fa-solid fa-arrow-up-right-from-square' style='font-size:0.75rem;'/>
        </button>
      </div>
    </header>

    <!-- KONDISI ERROR 404 BLOGGER -->
    <b:if cond='data:view.isError'>
      <div class='error-404-wrapper'>
        <div class='error-icon-box'><i class='fa-solid fa-compass-drafting'/></div>
        <div class='error-code'>404</div>
        <h1 class='error-title'>Halaman Tidak Ditemukan</h1>
        <p class='error-desc'>Halaman yang Anda tuju mungkin telah dipindahkan, dihapus, atau tidak tersedia sementara waktu.</p>
        <a class='error-btn-home' href='/'><i class='fa-solid fa-house'/> Kembali ke Beranda</a>
        <div class='error-timer'>Pengalihan otomatis dalam <span id='redirectCount' style='color:var(--accent-color); font-weight:bold;'>10</span> detik...</div>
      </div>

      <script type='text/javascript'>
        //<![CDATA[
          let seconds = 10;
          const timerEl = document.getElementById('redirectCount');
          const countdown = setInterval(() => {
            seconds--;
            if (timerEl) timerEl.innerText = seconds;
            if (seconds <= 0) {
              clearInterval(countdown);
              window.location.href = '/';
            }
          }, 1000);
        //]]>
      </script>
    <b:else/>

      <!-- MAIN CONTAINER -->
      <div class='container'>

        <!-- PROFIL & STORY AVATAR -->
        <div class='profile-section scroll-reveal' id='home'>
          <div class='avatar-container'>
            <div class='avatar-wrapper' onclick='openStoryModal()' title='Klik untuk melihat story status'>
              <img alt='Profile Avatar Gandzar Subagja' class='avatar-img' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQr_6Q2B6xIcyzYVfd3D5QpeH0YVaPzGM01Wgsp7msgcZ7X-dKoIdhdOFpO0gWdSxdaZhU-Tzzy_GyA39GF6svcSW9UK-1E39kZMqMjoNizs-Nv65xy_aY6vaFNh4MNiw5q5XphZbilf5uH6DUxQ0oMaGLMDtMK1E34r1GW5FCGVM0hskGWexFUDSZ7RA/s800/icon_untukdi_aboutthisapp.webp'/>
            </div>
            <button class='story-add-badge' onclick='openUploadStoryModal(event)' title='Tambah Story Baru (+)'><i class='fa-solid fa-plus'/></button>
          </div>

          <h1 class='profile-title'>Greetings! I&#39;m<br/><span class='highlight'>Gandzar Subagja</span> 👋</h1>
          
          <div class='typing-text-container'>
            <span class='typing-text' id='typingText'/><span class='cursor'/>
          </div>

          <p class='profile-bio'>Cuman Konten Kreator &amp; Fullstack Specialist biasa yang suka ngoprek sistem.</p>
          
          <div class='email-box'>
            <i class='fa-regular fa-envelope' style='color:var(--accent-color);'/>
            <span>gandzar@gmail.com</span>
            <button class='copy-btn' onclick='copyEmail()'><i class='fa-regular fa-copy'/> Salin</button>
          </div>

          <div class='profile-buttons'>
            <a class='btn-primary' href='#links'><i class='fa-solid fa-link'/> My Links</a>
            <a class='btn-secondary' href='#' onclick='openRecentCommentsModal()'><i class='fa-regular fa-comments'/> Diskusi</a>
            <button class='btn-secondary' onclick='shareProfile()'><i class='fa-solid fa-share-nodes'/></button>
          </div>
        </div>

        <!-- MULTI-VIEW SWITCHER TAB BAR (MERGE CONTROLLER) -->
        <div class='view-switcher-bar scroll-reveal'>
          <button class='view-tab-btn active' id='viewTabAll' onclick='switchBlogView("all")'>
            <i class='fa-solid fa-layer-group'/> Semua Fitur
          </button>
          <button class='view-tab-btn' id='viewTabSlider' onclick='switchBlogView("slider")'>
            <i class='fa-solid fa-panorama'/> 3D Slider
          </button>
          <button class='view-tab-btn' id='viewTabMarket' onclick='switchBlogView("market")'>
            <i class='fa-solid fa-shop'/> Marketplace
          </button>
          <button class='view-tab-btn' id='viewTabGallery' onclick='switchBlogView("gallery")'>
            <i class='fa-solid fa-images'/> Galeri 4-Kolom
          </button>
        </div>

        <!-- ==========================================
             SECTION 1: 3D COVERFLOW BLOG SLIDER
             ========================================== -->
        <div class='section-box scroll-reveal view-module' id='sliderSection' style='text-align:center;'>
          <div class='section-header-box' style='justify-content:center; flex-direction:column; align-items:center;'>
            <h2 class='section-title'><i class='fa-solid fa-wand-magic-sparkles' style='color:var(--accent-color);'/> Featured Showcase</h2>
            <p class='section-sub'>The app you open every day, not one you tolerate.</p>
          </div>
          
          <div class='slider-section-container'>
            <button class='slider-arrow-btn prev-arrow' onclick='moveSlide(-1)'><i class='fa-solid fa-chevron-left'/></button>
            <button class='slider-arrow-btn next-arrow' onclick='moveSlide(1)'><i class='fa-solid fa-chevron-right'/></button>

            <div class='slider-viewport'>
              <div class='slider-track' id='sliderTrack'>
                <div class='blog-card-empty' style='color:var(--text-sub); font-size:0.85rem; padding:30px;'>
                  <i class='fa-solid fa-spinner fa-spin' style='font-size:1.5rem; margin-bottom:8px; display:block;'/>
                  Memuat 3D coverflow slide...
                </div>
              </div>
            </div>

            <div class='slider-footer-controls'>
              <div class='slide-counter-badge' id='slideCounter'>01 / 01</div>
              <h3 class='section-title' id='slideActiveTitle' style='font-size:1.15rem; margin-top:4px;'>Settings Hub</h3>
              <p class='section-sub' id='slideActiveDesc' style='max-width:340px; font-size:0.8rem;'>Deskripsi ringkas dari postingan yang aktif.</p>

              <div class='slide-dots-wrapper' id='slideDots'/>

              <a class='download-apk-btn' href='#' id='downloadApkBtn'>
                <i class='fa-solid fa-download'/> Download APK / Buka
              </a>
            </div>
          </div>
        </div>

        <!-- ==========================================
             SECTION 2: MARKETPLACE HORIZONTAL CAROUSEL
             ========================================== -->
        <div class='section-box scroll-reveal view-module' id='marketplaceSection'>
          <div class='section-header-box'>
            <div>
              <h2 class='section-title'><i class='fa-solid fa-fire' style='color:#f97316;'/> Marketplace Catalog</h2>
              <p class='section-sub'>Geser ke samping untuk jelajahi item &amp; software</p>
            </div>
            <div class='slider-scroll-nav'>
              <button class='scroll-nav-btn' onclick='scrollMarketplaceTrack(-1)' title='Scroll Kiri'><i class='fa-solid fa-chevron-left'/></button>
              <button class='scroll-nav-btn' onclick='scrollMarketplaceTrack(1)' title='Scroll Kanan'><i class='fa-solid fa-chevron-right'/></button>
            </div>
          </div>

          <div class='marketplace-slider-wrapper'>
            <div class='marketplace-track' id='marketplaceTrack'>
              <div style='padding:25px; text-align:center; width:100%; color:var(--text-sub); font-size:0.82rem;'>
                <i class='fa-solid fa-spinner fa-spin'/> Memuat katalog marketplace...
              </div>
            </div>
          </div>
        </div>

        <!-- ==========================================
             SECTION 3: 4-COLUMN PHOTO & APP GALLERY GRID
             ========================================== -->
        <div class='section-box scroll-reveal view-module' id='gallerySection'>
          <div class='section-header-box' style='flex-direction:column; align-items:flex-start;'>
            <div style='width:100%; display:flex; justify-content:space-between; align-items:center;'>
              <h2 class='section-title'><i class='fa-solid fa-images' style='color:var(--accent-color);'/> Grid Galeri Foto &amp; Post</h2>
              <span id='galleryCountBadge' style='font-size:0.75rem; background:rgba(255,255,255,0.06); padding:3px 8px; border-radius:12px; color:var(--text-sub); font-weight:700;'>0 Item</span>
            </div>
            <p class='section-sub'>Tampilan grid presisi 4-kolom responsif dilengkapi pencarian instan</p>

            <!-- SEARCH BAR REALTIME -->
            <div class='search-box-container'>
              <i class='fa-solid fa-magnifying-glass search-icon-inside'/>
              <input class='search-input' id='searchInput' onkeyup='filterPostsBySearch()' placeholder='Cari artikel, file, atau keyword...' type='text'/>
              <button class='search-clear-btn' id='searchClearBtn' onclick='clearSearch()' title='Hapus Pencarian'><i class='fa-solid fa-xmark'/></button>
            </div>

            <!-- FILTER TAGS PILLS -->
            <div class='filter-tags-scroll' id='filterTagsContainer'>
              <button class='filter-tag-pill active' onclick='filterByCategory("semua", this)'>🌟 Semua</button>
              <button class='filter-tag-pill' onclick='filterByCategory("app", this)'>📱 Aplikasi</button>
              <button class='filter-tag-pill' onclick='filterByCategory("tutorial", this)'>🛠️ Tutorial</button>
              <button class='filter-tag-pill' onclick='filterByCategory("hardware", this)'>💻 Hardware</button>
              <button class='filter-tag-pill' onclick='filterByCategory("game", this)'>🎮 Game &amp; Boot</button>
            </div>
          </div>

          <!-- CONTAINER GRID 4-KOLOM -->
          <div class='gallery-grid-container' id='galleryGrid'>
            <div style='padding:35px 10px; text-align:center; grid-column: 1 / -1; color:var(--text-sub); font-size:0.85rem;'>
              <i class='fa-solid fa-spinner fa-spin' style='margin-right:6px;'/> Memuat galeri foto &amp; postingan...
            </div>
          </div>
        </div>

        <!-- BLOGGER NATIVE WIDGET HOOK (REQUIRED BY BLOGGER ENGINE) -->
        <b:section class='main' id='main' showaddelement='yes'>
          <b:widget id='Blog1' locked='true' title='Postingan Blog' type='Blog' version='2' visible='true'>
            <b:includable id='main'>
              <b:loop values='data:posts' var='post'>
                <article class='post' style='display:none;'>
                  <a expr:href='data:post.url'><data:post.title/></a>
                </article>
              </b:loop>
            </b:includable>
          </b:widget>
        </b:section>

        <!-- ==========================================
             SECTION 4: IMPORTANT LINKS & SOCIALS
             ========================================== -->
        <div class='section-box' id='links'>
          <h2 class='section-title scroll-reveal' style='text-align:center; justify-content:center;'>GNZX ShareLink to You!</h2>
          <p class='section-sub scroll-reveal' style='text-align:center;'>Semua link aplikasi &amp; download penting ada di sini.</p>

          <div class='social-links scroll-reveal'>
            <a class='social-icon' href='https://github.com' target='_blank' title='GitHub'><i class='fa-brands fa-github'/></a>
            <a class='social-icon' href='https://instagram.com' target='_blank' title='Instagram'><i class='fa-brands fa-instagram'/></a>
            <a class='social-icon' href='https://tiktok.com' target='_blank' title='TikTok'><i class='fa-brands fa-tiktok'/></a>
            <a class='social-icon' href='https://youtube.com' target='_blank' title='YouTube'><i class='fa-brands fa-youtube'/></a>
            <a class='social-icon' href='mailto:gandzar@gmail.com' title='Kirim Email'><i class='fa-regular fa-envelope'/></a>
          </div>

          <div class='links-list'>
            <a class='link-card scroll-reveal' href='#' onclick='openPostModal("link_1", "GNZX Downloader App", "Download GNZX Downloader App versi terbaru dengan kecepatan unduh maksimal dan bebas iklan.")'>
              <div class='card-left'>
                <div class='icon-box'><i class='fa-solid fa-cloud-arrow-down'/></div>
                <div class='card-info'>
                  <h3>GNZX Downloader</h3>
                  <p>Download GNZX Downloader App resmi disini</p>
                </div>
              </div>
              <i class='fa-solid fa-arrow-right arrow-icon'/>
            </a>

            <a class='link-card scroll-reveal' href='#' onclick='openPostModal("link_2", "Plana Boot Animation", "Download Plana Boot Animation spesial untuk smartphone Android dengan render halus 60fps.")'>
              <div class='card-left'>
                <div class='icon-box'><i class='fa-solid fa-mobile-screen-button'/></div>
                <div class='card-info'>
                  <h3>Plana Boot Animation</h3>
                  <p>Download Plana Boot Animation disini</p>
                </div>
              </div>
              <i class='fa-solid fa-arrow-right arrow-icon'/>
            </a>
          </div>
        </div>

        <!-- ==========================================
             SECTION 5: BLOG TRAFFIC STATS
             ========================================== -->
        <div class='section-box' id='traffic'>
          <h2 class='section-title scroll-reveal' style='text-align:center; justify-content:center;'>Blog Traffic &amp; Live Insight</h2>
          <p class='section-sub scroll-reveal' style='text-align:center;'>Statistik kunjungan &amp; data pengunjung realtime.</p>

          <div class='traffic-card scroll-reveal'>
            <div class='badge-live'>
              <span class='live-dot'/> Live Realtime Overview
            </div>
            
            <div class='stat-grid-top'>
              <div class='stat-box-item'>
                <div class='num' id='totalFollowers'>10</div>
                <div class='lbl'>Pengikut Aktif</div>
              </div>
              <div class='stat-box-item'>
                <div class='num' id='totalPosts'>0</div>
                <div class='lbl'>Postingan</div>
              </div>
              <div class='stat-box-item'>
                <div class='num' id='totalComments'>0</div>
                <div class='lbl'>Komentar</div>
              </div>
            </div>

            <div class='stat-list-detail'>
              <div class='stat-row'><span>Semua Kunjungan</span> <span class='val' id='viewsAll'>200</span></div>
              <div class='stat-row'><span>Hari Ini</span> <span class='val' id='viewsToday'>10</span></div>
              <div class='stat-row'><span>Kemarin</span> <span class='val' id='viewsYesterday'>13</span></div>
              <div class='stat-row'><span>Bulan Ini</span> <span class='val' id='viewsMonth'>55</span></div>
              <div class='stat-row'><span>Bulan Lalu</span> <span class='val' id='viewsLastMonth'>145</span></div>
            </div>
          </div>
        </div>

        <!-- FOOTER -->
        <footer>
          &#169; 2026 <b>Gandzar Subagja</b> - All rights reserved.<br/>
          Fullstack Developer - IT Support - Hardware Specialist
        </footer>

      </div>
    </b:if>

    <!-- AMBIENT AUDIO PLAYER ELEMENT -->
    <audio id='ambientAudio' loop='loop' src='https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3?filename=lofi-study-112191.mp3'/>

    <!-- ==========================================
         MODAL 1: FULLSCREEN STORY VIEWER
         ========================================== -->
    <div class='story-modal-overlay' id='storyModal'>
      <div class='story-card-box'>
        <div class='story-progress-container' id='storyProgressContainer'/>

        <div class='story-header'>
          <div class='story-user-info'>
            <img alt='Avatar' class='story-user-avatar' src='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhQr_6Q2B6xIcyzYVfd3D5QpeH0YVaPzGM01Wgsp7msgcZ7X-dKoIdhdOFpO0gWdSxdaZhU-Tzzy_GyA39GF6svcSW9UK-1E39kZMqMjoNizs-Nv65xy_aY6vaFNh4MNiw5q5XphZbilf5uH6DUxQ0oMaGLMDtMK1E34r1GW5FCGVM0hskGWexFUDSZ7RA/s800/icon_untukdi_aboutthisapp.webp'/>
            <div>
              <div class='story-username'>Gandzar Subagja</div>
              <div class='story-time' id='storyTime'><i class='fa-regular fa-clock'/> Baru saja</div>
            </div>
          </div>

          <div class='story-controls-top'>
            <button class='story-action-btn' onclick='downloadCurrentStory()' title='Download File Story'><i class='fa-solid fa-download'/></button>
            <button class='story-action-btn delete-btn' onclick='deleteCurrentStory()' title='Hapus Story Ini'><i class='fa-solid fa-trash-can'/></button>
            <button class='story-action-btn' onclick='closeStoryModalForce()'><i class='fa-solid fa-xmark'/></button>
          </div>
        </div>

        <div class='story-media-wrapper' id='storyMediaWrapper'/>

        <div class='story-nav-touch story-nav-left' onclick='prevStory()'/>
        <div class='story-nav-touch story-nav-right' onclick='nextStory()'/>

        <div class='story-caption-box' id='storyCaption'>Caption status story...</div>
      </div>
    </div>

    <!-- ==========================================
         MODAL 2: UPLOAD STORY (INDEXEDDB 100MB+)
         ========================================== -->
    <div class='upload-modal-overlay' id='uploadStoryModal' onclick='closeUploadStoryModal(event)'>
      <div class='upload-modal-box'>
        <div class='upload-title'><i class='fa-solid fa-circle-plus' style='color:var(--accent-color);'/> Tambah Story Baru</div>
        
        <div class='upload-field'>
          <label>File Foto / Video Galeri (Didukung s.d. 100MB+ via IndexedDB):</label>
          <input accept='image/*,video/mp4,video/webm,video/quicktime' id='storyFileInput' type='file'/>
        </div>

        <div class='upload-field'>
          <label>Atau Paste Direct URL Foto / Video MP4:</label>
          <input id='storyUrlInput' placeholder='https://... (URL Foto atau Video)' type='text'/>
        </div>

        <div class='upload-field'>
          <label>Caption / Pesan Status:</label>
          <textarea id='storyCaptionInput' placeholder='Tulis pesan status Anda disini...' rows='2'></textarea>
        </div>

        <div class='loading-status' id='loadingStatus'><i class='fa-solid fa-spinner fa-spin'/> Memproses &amp; Menyimpan Story ke database lokal...</div>

        <div style='display:flex; gap:8px; justify-content:flex-end; margin-top:6px;'>
          <button class='btn-secondary' id='btnCancelUpload' onclick='closeUploadStoryModalForce()' style='padding:8px 14px;'>Batal</button>
          <button class='btn-primary' id='btnSaveUpload' onclick='saveNewStory()' style='padding:8px 16px;'>Simpan Story</button>
        </div>
      </div>
    </div>

    <!-- ==========================================
         MODAL 3: FULL POST READING & MODERN COMMENT
         ========================================== -->
    <div class='post-modal-overlay' id='postModal' onclick='closePostModal(event)'>
      <div class='post-modal-container'>
        <button class='post-modal-close' onclick='closePostModalForce()'><i class='fa-solid fa-xmark'/></button>
        
        <div class='post-modal-header'>
          <div class='post-meta-bar'>
            <span class='post-meta-item'><i class='fa-regular fa-calendar'/> <span id='modalPostDate'>Hari ini</span></span>
            <span class='post-meta-item'><i class='fa-regular fa-clock'/> <span id='modalReadingTime'>1 menit baca</span></span>
            <span class='post-meta-item'><i class='fa-solid fa-user-pen'/> Gandzar Subagja</span>
          </div>
          <h2 class='post-modal-title' id='modalTitle'>Judul Postingan</h2>
        </div>

        <!-- READER TOOLBAR (TTS, ZOOM, SHARE) -->
        <div class='reader-toolbar'>
          <button class='tts-btn' id='ttsButton' onclick='toggleSpeechReader()'>
            <i class='fa-solid fa-volume-high' id='ttsIcon'/> <span id='ttsLabel'>Dengarkan Artikel</span>
          </button>
          <div class='font-zoom-group'>
            <span style='font-size:0.75rem; color:var(--text-sub);'>Teks:</span>
            <button class='font-zoom-btn' onclick='zoomPostText(-1)'>A-</button>
            <button class='font-zoom-btn' onclick='zoomPostText(1)'>A+</button>
          </div>
        </div>

        <div class='post-modal-body' id='modalBody'>Isi postingan akan dimuat disini...</div>
        
        <div class='modal-action-bar'>
          <div class='action-btn-group'>
            <button class='like-btn' id='modalLikeBtn' onclick='toggleLikeFromModal(event)'>
              <i class='fa-regular fa-heart' id='modalLikeIcon'/>
              <span id='modalLikeCount'>0</span> Suka
            </button>

            <button class='follow-btn' id='modalFollowBtn' onclick='toggleFollowGlobal(event)'>
              <i class='fa-solid fa-user-plus' id='modalFollowIcon'/>
              <span id='modalFollowText'>Ikuti</span>
            </button>
          </div>
          
          <button class='share-love-btn' onclick='shareToLovedOne()'>
            <i class='fa-solid fa-share-nodes' style='color:var(--accent-color);'/> Bagikan ke Teman
          </button>
        </div>

        <!-- KOLOM KOMENTAR MODERN TERINTEGRASI -->
        <div class='comments-section'>
          <div class='comments-title'><i class='fa-regular fa-comments'/> Kolom Komentar Interaktif</div>
          
          <div class='comment-input-box'>
            <input id='commentName' placeholder='Nama Anda (opsional)...' type='text'/>
            <textarea id='commentText' placeholder='Tulis tanggapan atau pertanyaan Anda disini...'></textarea>
            
            <div class='comment-form-actions'>
              <button class='cancel-edit-btn' id='cancelEditBtn' onclick='cancelCommentEdit()'><i class='fa-solid fa-xmark'/> Batal Edit</button>
              <button class='comment-submit-btn' id='commentSubmitBtn' onclick='addModalComment()'>Kirim Komentar</button>
            </div>
          </div>

          <div class='comments-list' id='modalCommentsList'/>
        </div>
      </div>
    </div>

    <!-- ==========================================
         MODAL 4: RECENT COMMENTS DIALOG
         ========================================== -->
    <div class='post-modal-overlay' id='recentCommentsModal' onclick='closeRecentCommentsModal(event)'>
      <div class='post-modal-container'>
        <button class='post-modal-close' onclick='closeRecentCommentsModalForce()'><i class='fa-solid fa-xmark'/></button>
        <h2 class='post-modal-title' style='margin-bottom:6px;'><i class='fa-regular fa-comments' style='color:var(--accent-color);'/> Komentar Terbaru</h2>
        <p class='section-sub' style='text-align:left; margin-bottom:15px;'>Komentar &amp; diskusi terkini dari pengunjung blog:</p>
        
        <div class='comments-widget-list' id='recentCommentsListModal' style='max-height: 420px; overflow-y: auto; display: flex; flex-direction: column; gap: 10px;'>
          <div style='text-align:center; font-size:0.8rem; color:var(--text-sub); padding:20px;'>
            <i class='fa-solid fa-spinner fa-spin' style='margin-right:6px;'/> Memuat daftar komentar...
          </div>
        </div>
      </div>
    </div>

    <!-- TOAST CONTAINER -->
    <div class='toast-container' id='toastContainer'/>

    <!-- TOUCH RIPPLE RING CONTAINER -->
    <div class='touch-container' id='touchContainer'/>

    <!-- JAVASCRIPT MASTER LOGIC -->
    <script type='text/javascript'>
      //<![CDATA[
        /* KONFIGURASI PENGATURAN BLOG */
        const FORMSPREE_ENDPOINT_ID = 'mvkzpprq'; // Ganti dengan ID Formspree Anda jika diperlukan

        /* STATE VARIABLES */
        let db;
        const DB_NAME = "BlogStoryDB";
        const STORE_NAME = "stories";

        let storyList = [];
        let storyIndex = 0;
        let storyTimer = null;
        let storyProgressInterval = null;
        let currentProgress = 0;

        let particleInterval;
        let currentAnimType = localStorage.getItem('bgAnimType') || 'leaf';
        let particleSpeed = parseInt(localStorage.getItem('bgAnimSpeed')) || 300;
        let isBubblesOn = localStorage.getItem('bubbles_enabled') !== 'false';

        let allPostsData = [];
        let currentActivePostId = '';
        let editingCommentIndex = null;
        let currentSlideIdx = 0;
        let slideItems = [];
        let currentPostFontSize = 14.4; // 0.9rem
        let isSpeaking = false;

        /* INITIALIZATION PADA DOM READY */
        document.addEventListener("DOMContentLoaded", function () {
            // Pulihkan konfigurasi tersimpan
            const savedPreset = localStorage.getItem('themePreset') || 'default';
            applyThemePreset(savedPreset, false);

            const savedFontSize = localStorage.getItem('fontSize');
            if (savedFontSize) document.documentElement.style.setProperty('--base-font-size', savedFontSize);

            const savedFontFamily = localStorage.getItem('fontFamily');
            if (savedFontFamily) setFontFamily(savedFontFamily, false);

            const savedCustomBg = localStorage.getItem('custom_bg_val');
            if (savedCustomBg) {
                if (savedCustomBg.startsWith('http') || savedCustomBg.startsWith('data:image')) {
                    document.body.style.backgroundImage = `url('${savedCustomBg}')`;
                } else {
                    document.body.style.background = savedCustomBg;
                }
            }

            const savedBlur = localStorage.getItem('glass_blur_val');
            if (savedBlur) document.documentElement.style.setProperty('--glass-blur', savedBlur);

            setBgAnimation(isBubblesOn ? currentAnimType : 'none', false);
            syncBubbleUI();
            initLikesAndStats();
            syncFollowUI();
            initIndexedDB();
            loadBloggerFeeds();
            initScrollReveal();
        });

        /* ========================================================
           INDEXEDDB UNTUK STORY BESAR (HINGGA 100MB+)
           ======================================================== */
        function initIndexedDB() {
            if (!window.indexedDB) return;
            const request = indexedDB.open(DB_NAME, 1);
            request.onupgradeneeded = function (e) {
                db = e.target.result;
                if (!db.objectStoreNames.contains(STORE_NAME)) {
                    db.createObjectStore(STORE_NAME, { keyPath: "id", autoIncrement: true });
                }
            };
            request.onsuccess = function (e) {
                db = e.target.result;
            };
        }

        function loadStoriesFromDB(callback) {
            if (!db) {
                setTimeout(() => loadStoriesFromDB(callback), 200);
                return;
            }
            const tx = db.transaction(STORE_NAME, "readonly");
            const store = tx.objectStore(STORE_NAME);
            const request = store.getAll();
            request.onsuccess = function () {
                storyList = request.result || [];
                if (callback) callback();
            };
        }

        function addStoryToDB(storyObj, callback) {
            const tx = db.transaction(STORE_NAME, "readwrite");
            const store = tx.objectStore(STORE_NAME);
            const request = store.add(storyObj);
            request.onsuccess = function () {
                if (callback) callback();
            };
        }

        function deleteStoryFromDB(id, callback) {
            const tx = db.transaction(STORE_NAME, "readwrite");
            const store = tx.objectStore(STORE_NAME);
            const request = store.delete(id);
            request.onsuccess = function () {
                if (callback) callback();
            };
        }

        /* STORY VIEWER LOGIC */
        function openStoryModal() {
            loadStoriesFromDB(() => {
                if (storyList.length === 0) {
                    showToast("Belum ada story status. Silakan tambahkan baru!", "info");
                    openUploadStoryModal();
                    return;
                }
                storyIndex = 0;
                document.getElementById('storyModal').classList.add('active');
                document.body.style.overflow = 'hidden';
                setupStorySegments();
                showStoryContent();
            });
        }

        function setupStorySegments() {
            const container = document.getElementById('storyProgressContainer');
            if(!container) return;
            container.innerHTML = '';
            storyList.forEach((_, idx) => {
                const seg = document.createElement('div');
                seg.className = 'story-progress-segment';
                seg.innerHTML = `<div class="story-progress-fill" id="storyProgressFill_${idx}"></div>`;
                container.appendChild(seg);
            });
        }

        function showStoryContent() {
            clearInterval(storyProgressInterval);
            clearTimeout(storyTimer);

            storyList.forEach((_, idx) => {
                const fill = document.getElementById(`storyProgressFill_${idx}`);
                if (!fill) return;
                if (idx < storyIndex) fill.style.width = '100%';
                else fill.style.width = '0%';
            });

            const currentStory = storyList[storyIndex];
            const mediaWrapper = document.getElementById('storyMediaWrapper');
            if (!mediaWrapper || !currentStory) return;
            mediaWrapper.innerHTML = '';

            document.getElementById('storyCaption').innerText = currentStory.caption || '';
            document.getElementById('storyTime').innerHTML = `<i class="fa-regular fa-clock"></i> ${currentStory.time || 'Baru saja'}`;

            let duration = 5000;
            let mediaUrl = currentStory.url;
            if (currentStory.fileBlob) {
                mediaUrl = URL.createObjectURL(currentStory.fileBlob);
            }

            if (currentStory.type === 'video') {
                const videoEl = document.createElement('video');
                videoEl.src = mediaUrl;
                videoEl.autoplay = true;
                videoEl.playsInline = true;

                videoEl.onloadedmetadata = function() {
                    if (videoEl.duration && !isNaN(videoEl.duration)) {
                        duration = Math.max(videoEl.duration * 1000, 3000);
                    }
                    startStoryTimer(duration);
                };
                videoEl.onerror = function() { startStoryTimer(4000); };
                mediaWrapper.appendChild(videoEl);
            } else {
                const imgEl = document.createElement('img');
                imgEl.src = mediaUrl;
                mediaWrapper.appendChild(imgEl);
                startStoryTimer(duration);
            }
        }

        function startStoryTimer(duration) {
            currentProgress = 0;
            const currentFill = document.getElementById(`storyProgressFill_${storyIndex}`);
            const stepTime = 50;
            const increment = (stepTime / duration) * 100;

            storyProgressInterval = setInterval(() => {
                currentProgress += increment;
                if (currentFill) currentFill.style.width = Math.min(currentProgress, 100) + '%';

                if (currentProgress >= 100) {
                    clearInterval(storyProgressInterval);
                    nextStory();
                }
            }, stepTime);
        }

        function nextStory() {
            if (storyIndex < storyList.length - 1) {
                storyIndex++;
                showStoryContent();
            } else {
                closeStoryModalForce();
            }
        }

        function prevStory() {
            if (storyIndex > 0) {
                storyIndex--;
                showStoryContent();
            } else {
                showStoryContent();
            }
        }

        function closeStoryModalForce() {
            clearInterval(storyProgressInterval);
            clearTimeout(storyTimer);
            document.getElementById('storyModal').classList.remove('active');
            document.body.style.overflow = 'auto';

            const mediaWrapper = document.getElementById('storyMediaWrapper');
            if (mediaWrapper) mediaWrapper.innerHTML = '';
        }

        function deleteCurrentStory() {
            if (!confirm("Apakah Anda yakin ingin menghapus story ini?")) return;
            const targetStory = storyList[storyIndex];
            if (!targetStory) return;

            deleteStoryFromDB(targetStory.id, () => {
                showToast("Story berhasil dihapus", "info");
                loadStoriesFromDB(() => {
                    if (storyList.length === 0) {
                        closeStoryModalForce();
                    } else {
                        if (storyIndex >= storyList.length) storyIndex = storyList.length - 1;
                        setupStorySegments();
                        showStoryContent();
                    }
                });
            });
        }

        function downloadCurrentStory() {
            const currentStory = storyList[storyIndex];
            if (!currentStory) return;

            let downloadUrl = currentStory.url;
            if (currentStory.fileBlob) {
                downloadUrl = URL.createObjectURL(currentStory.fileBlob);
            }

            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = `Story_GNZX_${Date.now()}.${currentStory.type === 'video' ? 'mp4' : 'jpg'}`;
            document.body.appendChild(a);
            a.click();
            a.remove();
            showToast("Mengunduh story...", "success");
        }

        function openUploadStoryModal(e) {
            if (e) e.stopPropagation();
            document.getElementById('uploadStoryModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeUploadStoryModal(e) {
            if (e.target.id === 'uploadStoryModal') closeUploadStoryModalForce();
        }

        function closeUploadStoryModalForce() {
            document.getElementById('uploadStoryModal').classList.remove('active');
            document.body.style.overflow = 'auto';
            document.getElementById('storyFileInput').value = '';
            document.getElementById('storyUrlInput').value = '';
            document.getElementById('storyCaptionInput').value = '';
            document.getElementById('loadingStatus').style.display = 'none';
        }

        function getCurrentTimeString() {
            const now = new Date();
            const hours = String(now.getHours()).padStart(2, '0');
            const minutes = String(now.getMinutes()).padStart(2, '0');
            return `${hours}:${minutes} WIB`;
        }

        function saveNewStory() {
            const fileInput = document.getElementById('storyFileInput');
            const urlInput = document.getElementById('storyUrlInput').value.trim();
            const captionInput = document.getElementById('storyCaptionInput').value.trim();
            const timeFormatted = getCurrentTimeString();

            if (fileInput.files && fileInput.files[0]) {
                const file = fileInput.files[0];
                const isVideo = file.type.startsWith('video/');

                document.getElementById('loadingStatus').style.display = 'block';

                const newStoryObj = {
                    type: isVideo ? 'video' : 'image',
                    fileBlob: file,
                    caption: captionInput || (isVideo ? 'Video Story' : 'Photo Story'),
                    time: timeFormatted
                };

                addStoryToDB(newStoryObj, () => {
                    closeUploadStoryModalForce();
                    showToast("Story berhasil diunggah!", "success");
                    openStoryModal();
                });
            } else if (urlInput) {
                const isVideo = urlInput.endsWith('.mp4') || urlInput.endsWith('.webm') || urlInput.includes('video');
                const newStoryObj = {
                    type: isVideo ? 'video' : 'image',
                    url: urlInput,
                    caption: captionInput || 'Story Status',
                    time: timeFormatted
                };

                addStoryToDB(newStoryObj, () => {
                    closeUploadStoryModalForce();
                    showToast("Story berhasil ditambahkan!", "success");
                    openStoryModal();
                });
            } else {
                showToast("Pilih file foto/video atau masukkan URL terlebih dahulu.", "info");
            }
        }

        /* ========================================================
           MULTI-VIEW SWITCHER CONTROLLER
           ======================================================== */
        function switchBlogView(viewMode) {
            document.querySelectorAll('.view-tab-btn').forEach(btn => btn.classList.remove('active'));
            
            const activeBtn = document.getElementById('viewTab' + capitalize(viewMode));
            if (activeBtn) activeBtn.classList.add('active');

            const sliderSec = document.getElementById('sliderSection');
            const marketSec = document.getElementById('marketplaceSection');
            const gallerySec = document.getElementById('gallerySection');

            if (viewMode === 'all') {
                if (sliderSec) sliderSec.style.display = 'block';
                if (marketSec) marketSec.style.display = 'block';
                if (gallerySec) gallerySec.style.display = 'block';
            } else if (viewMode === 'slider') {
                if (sliderSec) sliderSec.style.display = 'block';
                if (marketSec) marketSec.style.display = 'none';
                if (gallerySec) gallerySec.style.display = 'none';
            } else if (viewMode === 'market') {
                if (sliderSec) sliderSec.style.display = 'none';
                if (marketSec) marketSec.style.display = 'block';
                if (gallerySec) gallerySec.style.display = 'none';
            } else if (viewMode === 'gallery') {
                if (sliderSec) sliderSec.style.display = 'none';
                if (marketSec) marketSec.style.display = 'none';
                if (gallerySec) gallerySec.style.display = 'block';
            }
        }

        function capitalize(s) {
            return s.charAt(0).toUpperCase() + s.slice(1);
        }

        /* ========================================================
           LOAD BLOGGER POSTS FEED & FALLBACK GENERATOR
           ======================================================== */
        function loadBloggerFeeds() {
            fetch('/feeds/posts/default?alt=json&max-results=50')
                .then(res => {
                    if (!res.ok) throw new Error("Status " + res.status);
                    return res.json();
                })
                .then(data => {
                    const entries = (data.feed && data.feed.entry) ? data.feed.entry : [];
                    if (entries.length > 0) {
                        processFeedEntries(entries);
                    } else {
                        loadFallbackPosts();
                    }
                })
                .catch(err => {
                    console.log("Memuat data demo lokal untuk preview responsif:", err);
                    loadFallbackPosts();
                });
        }

        function loadFallbackPosts() {
            const demoPosts = [
                {
                    postId: 'demo_1',
                    title: 'GNZX Downloader v4.2 Pro Edition',
                    body: '<p>Aplikasi downloader mutakhir dengan multi-threading engine, converter MP3 otomatis, dan integrasi cloud storage. Mendukung pengunduhan dari puluhan platform video terkemuka dengan kualitas hingga 4K Ultra HD tanpa watermark.</p><img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop" alt="Downloader Pro"/><p>Fitur Utama:</p><ul><li>Download batch simultan</li><li>Resume otomatis saat jaringan terputus</li><li>Dark mode hemat daya</li></ul>',
                    imgSrc: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop',
                    isLatestPost: true,
                    cleanText: 'aplikasi downloader mutakhir dengan multi-threading converter mp3 4k ultra hd app download',
                    category: 'app'
                },
                {
                    postId: 'demo_2',
                    title: 'Plana Boot Animation Android 60FPS',
                    body: '<p>Kustomisasi boot animation karakter Plana eksklusif dengan refresh rate tinggi 60 FPS. Memberikan sensasi booting ponsel Android Anda terlihat lebih estetik, futuristik, dan memukau setiap kali dinyalakan.</p><img src="https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop" alt="Boot Animation"/><p>Cara pasang cukup replace file bootanimation.zip pada direktori system media.</p>',
                    imgSrc: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop',
                    isLatestPost: false,
                    cleanText: 'plana boot animation android 60fps kustomisasi sistem rooting magisk game',
                    category: 'game'
                },
                {
                    postId: 'demo_3',
                    title: 'Optimalisasi Thermal Pasta & Pendingin Laptop Gaming',
                    body: '<p>Panduan lengkap perawatan hardware: cara mengganti thermal paste jenis liquid metal dan phase change pad pada laptop gaming agar suhu prosesor turun hingga 15 derajat Celsius dalam beban kerja berat.</p><img src="https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=800&auto=format&fit=crop" alt="Hardware Cleaning"/><p>Langkah detail pencegahan overheat dan thermal throttling pada CPU & GPU modern.</p>',
                    imgSrc: 'https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?w=800&auto=format&fit=crop',
                    isLatestPost: false,
                    cleanText: 'optimalisasi thermal pasta pendingin laptop gaming hardware servis cpu gpu',
                    category: 'hardware'
                },
                {
                    postId: 'demo_4',
                    title: 'Tutorial Lengkap Modding ROM & Magisk Module',
                    body: '<p>Kupas tuntas modifikasi custom kernel, governor tweak, dan instalasi module magisk untuk performa gaming tanpa lag serta daya tahan baterai seharian.</p><img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop" alt="Code Modding"/><p>Termasuk cara backup IMEI dan partisi EFS sebelum melakukan flashing.</p>',
                    imgSrc: 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop',
                    isLatestPost: false,
                    cleanText: 'tutorial lengkap modding rom magisk module custom kernel android gaming tutorial',
                    category: 'tutorial'
                },
                {
                    postId: 'demo_5',
                    title: 'Cyber Security Essentials: Amankan Data Pribadi',
                    body: '<p>Trik mencegah social engineering, phishing, dan cara setup 2FA berbasis hardware security key YubiKey pada semua akun penting Anda.</p><img src="https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800&auto=format&fit=crop" alt="Security"/><p>Pentingnya enkripsi end-to-end dan DNS over HTTPS.</p>',
                    imgSrc: 'https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800&auto=format&fit=crop',
                    isLatestPost: false,
                    cleanText: 'cyber security essentials data pribadi yubikey 2fa enkripsi tutorial',
                    category: 'tutorial'
                }
            ];

            allPostsData = demoPosts;
            renderAllSections();
        }

        function processFeedEntries(entries) {
            allPostsData = entries.map((entry, idx) => {
                const title = entry.title.$t;
                const body = entry.content ? entry.content.$t : (entry.summary ? entry.summary.$t : '');
                const postId = entry.id.$t.split('post-')[1] || ('post_' + idx);
                const isLatestPost = (idx === 0);

                let imgSrc = 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop';
                if (entry.media$thumbnail) {
                    imgSrc = entry.media$thumbnail.url.replace('/s72-c/', '/w600/');
                } else {
                    const tempDiv = document.createElement('div');
                    tempDiv.innerHTML = body;
                    const img = tempDiv.querySelector('img');
                    if (img) imgSrc = img.src;
                }

                const tempDiv = document.createElement('div');
                tempDiv.innerHTML = body;
                const cleanText = (tempDiv.textContent || tempDiv.innerText || '').toLowerCase();

                let category = 'app';
                if (cleanText.includes('tutorial') || cleanText.includes('cara')) category = 'tutorial';
                else if (cleanText.includes('hardware') || cleanText.includes('laptop') || cleanText.includes('komputer')) category = 'hardware';
                else if (cleanText.includes('game') || cleanText.includes('boot')) category = 'game';

                return {
                    postId,
                    title,
                    body,
                    imgSrc,
                    isLatestPost,
                    cleanText,
                    category
                };
            });

            renderAllSections();
        }

        function renderAllSections() {
            document.getElementById('totalPosts').innerText = allPostsData.length;
            const galleryCount = document.getElementById('galleryCountBadge');
            if (galleryCount) galleryCount.innerText = `${allPostsData.length} Item`;

            render3DSlider(allPostsData);
            renderMarketplaceTrack(allPostsData);
            renderGalleryGrid(allPostsData);
            updateTotalCommentsCount();
        }

        /* ========================================================
           RENDERER 1: 3D COVERFLOW SLIDER
           ======================================================== */
        function render3DSlider(posts) {
            const track = document.getElementById('sliderTrack');
            if (!track) return;
            track.innerHTML = '';

            if (posts.length === 0) {
                track.innerHTML = `<div class="blog-card-empty" style="color:var(--text-sub);"><p>Belum Ada Postingan</p></div>`;
                return;
            }

            const isUserFollowing = localStorage.getItem('is_following_blog') === 'true';

            posts.forEach((post, idx) => {
                const likesData = JSON.parse(localStorage.getItem('post_likes_data') || '{}');
                const isLiked = likesData[post.postId] ? likesData[post.postId].userLiked : false;
                const likeCount = likesData[post.postId] ? likesData[post.postId].count : 0;
                const snippet = post.cleanText.substring(0, 80) + '...';

                const card = document.createElement('div');
                card.className = 'slide-card-item';
                card.setAttribute('data-postid', post.postId);
                card.setAttribute('data-title', post.title);
                card.setAttribute('data-desc', snippet);

                card.innerHTML = `
                    ${post.isLatestPost ? `<div class="card-new-badge">NEW 🔴</div>` : ''}
                    <img class="slide-card-thumb" src="${post.imgSrc}" alt="${post.title}" loading="lazy"/>
                    <h3 class="slide-card-title">${post.title}</h3>
                    <div class="slide-card-snippet">${snippet}</div>
                    <div class="card-like-bar">
                      <button class="like-btn ${isLiked ? 'liked' : ''}" id="likeBtn_${post.postId}" onclick="toggleLike(event, '${post.postId}')">
                        <i class="fa-${isLiked ? 'solid' : 'regular'} fa-heart"></i>
                        <span class="like-count">${likeCount}</span>
                      </button>
                      <button class="follow-btn ${isUserFollowing ? 'following' : ''}" onclick="toggleFollowGlobal(event)">
                        <i class="fa-solid fa-${isUserFollowing ? 'user-check' : 'user-plus'}"></i>
                        <span class="follow-text">${isUserFollowing ? 'Mengikuti' : 'Ikuti'}</span>
                      </button>
                    </div>
                `;

                card.onclick = function(e) {
                    if (e.target.closest('.like-btn') || e.target.closest('.follow-btn')) return;
                    if (card.classList.contains('active')) {
                        openPostModal(post.postId, post.title, post.body);
                    } else {
                        currentSlideIdx = idx;
                        updateSlidePositions();
                    }
                };

                track.appendChild(card);
            });

            slideItems = document.querySelectorAll('.slide-card-item');
            buildDots();
            updateSlidePositions();
        }

        function updateSlidePositions() {
            if (slideItems.length === 0) return;

            slideItems.forEach((item, i) => {
                item.classList.remove('active', 'prev', 'next');
                if (i === currentSlideIdx) item.classList.add('active');
                else if (i === (currentSlideIdx - 1 + slideItems.length) % slideItems.length) item.classList.add('prev');
                else if (i === (currentSlideIdx + 1) % slideItems.length) item.classList.add('next');
            });

            const numStr = String(currentSlideIdx + 1).padStart(2, '0');
            const totalStr = String(slideItems.length).padStart(2, '0');
            const counterEl = document.getElementById('slideCounter');
            if (counterEl) counterEl.innerText = `${numStr} / ${totalStr}`;

            const activeCard = slideItems[currentSlideIdx];
            if (activeCard) {
                const titleEl = document.getElementById('slideActiveTitle');
                const descEl = document.getElementById('slideActiveDesc');
                const apkBtn = document.getElementById('downloadApkBtn');

                const title = activeCard.getAttribute('data-title');
                const desc = activeCard.getAttribute('data-desc');
                const postId = activeCard.getAttribute('data-postid');

                if (titleEl) titleEl.innerText = title;
                if (descEl) descEl.innerText = desc;
                if (apkBtn) {
                    apkBtn.onclick = function(e) {
                        e.preventDefault();
                        const targetPost = allPostsData.find(p => p.postId === postId);
                        if (targetPost) openPostModal(targetPost.postId, targetPost.title, targetPost.body);
                    };
                }
            }

            document.querySelectorAll('.slide-dot-item').forEach((dot, idx) => {
                dot.classList.toggle('active', idx === currentSlideIdx);
            });
        }

        function moveSlide(dir) {
            if (slideItems.length === 0) return;
            currentSlideIdx = (currentSlideIdx + dir + slideItems.length) % slideItems.length;
            updateSlidePositions();
        }

        function buildDots() {
            const dotsWrapper = document.getElementById('slideDots');
            if (!dotsWrapper) return;
            dotsWrapper.innerHTML = '';
            slideItems.forEach((_, idx) => {
                const dot = document.createElement('div');
                dot.className = 'slide-dot-item';
                dot.onclick = () => {
                    currentSlideIdx = idx;
                    updateSlidePositions();
                };
                dotsWrapper.appendChild(dot);
            });
        }

        /* ========================================================
           RENDERER 2: MARKETPLACE HORIZONTAL TRACK
           ======================================================== */
        function renderMarketplaceTrack(posts) {
            const track = document.getElementById('marketplaceTrack');
            if (!track) return;
            track.innerHTML = '';

            if (posts.length === 0) {
                track.innerHTML = `<div style="padding:20px; text-align:center; width:100%; color:var(--text-sub);">Belum Ada Item</div>`;
                return;
            }

            const isUserFollowing = localStorage.getItem('is_following_blog') === 'true';

            posts.forEach((post, idx) => {
                const snippet = post.cleanText.substring(0, 65) + '...';
                const likesData = JSON.parse(localStorage.getItem('post_likes_data') || '{}');
                const isLiked = likesData[post.postId] ? likesData[post.postId].userLiked : false;
                const likeCount = likesData[post.postId] ? likesData[post.postId].count : 0;

                const card = document.createElement('div');
                card.className = 'market-card';
                card.setAttribute('data-postid', post.postId);
                card.setAttribute('data-title', post.title);

                card.innerHTML = `
                    <div class="market-card-thumb-box">
                      ${post.isLatestPost ? `<span class="card-badge-tag">HOT 🔥</span>` : `<span class="card-badge-tag" style="background:rgba(0,0,0,0.65);">PRO</span>`}
                      <img class="market-card-thumb" src="${post.imgSrc}" alt="${post.title}" loading="lazy"/>
                    </div>
                    <div class="market-card-content">
                      <h3 class="market-card-title">${post.title}</h3>
                      <p class="market-card-desc">${snippet}</p>
                    </div>
                    <div class="market-card-footer">
                      <button class="like-btn ${isLiked ? 'liked' : ''}" id="marketLikeBtn_${post.postId}" onclick="toggleLike(event, '${post.postId}')">
                        <i class="fa-${isLiked ? 'solid' : 'regular'} fa-heart"></i>
                        <span class="like-count">${likeCount}</span>
                      </button>
                      <button class="follow-btn ${isUserFollowing ? 'following' : ''}" onclick="toggleFollowGlobal(event)">
                        <i class="fa-solid fa-${isUserFollowing ? 'user-check' : 'user-plus'}"></i>
                      </button>
                    </div>
                `;

                card.onclick = function(e) {
                    if (e.target.closest('.like-btn') || e.target.closest('.follow-btn')) return;
                    openPostModal(post.postId, post.title, post.body);
                };

                track.appendChild(card);
            });
        }

        function scrollMarketplaceTrack(direction) {
            const track = document.getElementById('marketplaceTrack');
            if (track) {
                const scrollAmount = 210 * direction;
                track.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }
        }

        /* ========================================================
           RENDERER 3: 4-COLUMN PHOTO & APP GALLERY GRID
           ======================================================== */
        function renderGalleryGrid(posts) {
            const grid = document.getElementById('galleryGrid');
            if (!grid) return;
            grid.innerHTML = '';

            if (posts.length === 0) {
                grid.innerHTML = `
                    <div style="grid-column: 1 / -1; text-align:center; padding:40px 10px; color:var(--text-sub);">
                        <i class="fa-solid fa-magnifying-glass" style="font-size:2rem; margin-bottom:10px; opacity:0.4;"></i>
                        <p style="font-size:0.85rem;">Tidak ada postingan yang sesuai pencarian.</p>
                    </div>`;
                return;
            }

            posts.forEach(post => {
                const card = document.createElement('div');
                card.className = 'gallery-card';
                card.setAttribute('data-postid', post.postId);
                card.setAttribute('data-title', post.title);

                card.innerHTML = `
                    <img class="gallery-thumb" src="${post.imgSrc}" alt="${post.title}" loading="lazy"/>
                    ${post.isLatestPost ? `<div class="gallery-badge"><i class="fa-solid fa-fire" style="color:#ef4444;"></i> NEW</div>` : ''}
                    <div class="gallery-overlay">
                        <div class="gallery-title">${post.title}</div>
                    </div>
                `;

                card.onclick = function() {
                    openPostModal(post.postId, post.title, post.body);
                };

                grid.appendChild(card);
            });
        }

        function filterPostsBySearch() {
            const input = document.getElementById('searchInput');
            const clearBtn = document.getElementById('searchClearBtn');
            const query = input.value.toLowerCase().trim();

            if (clearBtn) clearBtn.style.display = query ? 'block' : 'none';

            if (!query) {
                renderGalleryGrid(allPostsData);
                return;
            }

            const filtered = allPostsData.filter(post => {
                return post.title.toLowerCase().includes(query) || post.cleanText.includes(query);
            });

            renderGalleryGrid(filtered);
        }

        function clearSearch() {
            const input = document.getElementById('searchInput');
            if (input) {
                input.value = '';
                filterPostsBySearch();
            }
        }

        function filterByCategory(cat, btnEl) {
            document.querySelectorAll('.filter-tag-pill').forEach(b => b.classList.remove('active'));
            if (btnEl) btnEl.classList.add('active');

            if (cat === 'semua') {
                renderGalleryGrid(allPostsData);
                return;
            }

            const filtered = allPostsData.filter(post => post.category === cat);
            renderGalleryGrid(filtered);
        }

        /* ========================================================
           GLOBAL LIKE & FOLLOW SYNCHRONIZATION
           ======================================================== */
        function toggleFollowGlobal(e) {
            if (e) e.stopPropagation();
            let isFollowing = localStorage.getItem('is_following_blog') === 'true';
            isFollowing = !isFollowing;

            localStorage.setItem('is_following_blog', isFollowing ? 'true' : 'false');
            
            let baseFollowers = parseInt(localStorage.getItem('bg_base_followers') || '10');
            let currentFollowerCount = isFollowing ? (baseFollowers + 1) : baseFollowers;
            localStorage.setItem('bg_total_followers', currentFollowerCount);

            syncFollowUI();
            showToast(isFollowing ? "Berhasil mengikuti blog! Terima kasih ❤️" : "Berhenti mengikuti blog.", "info");
        }

        function syncFollowUI() {
            const isFollowing = localStorage.getItem('is_following_blog') === 'true';
            const followerCount = localStorage.getItem('bg_total_followers') || '10';

            const totalFollowersEl = document.getElementById('totalFollowers');
            if (totalFollowersEl) totalFollowersEl.innerText = followerCount;

            document.querySelectorAll('.follow-btn').forEach(btn => {
                if (btn.id !== 'modalFollowBtn') {
                    const icon = btn.querySelector('i');
                    const text = btn.querySelector('.follow-text');
                    if (isFollowing) {
                        btn.classList.add('following');
                        if (icon) icon.className = 'fa-solid fa-user-check';
                        if (text) text.innerText = 'Mengikuti';
                    } else {
                        btn.classList.remove('following');
                        if (icon) icon.className = 'fa-solid fa-user-plus';
                        if (text) text.innerText = 'Ikuti';
                    }
                }
            });

            const modalBtn = document.getElementById('modalFollowBtn');
            const modalIcon = document.getElementById('modalFollowIcon');
            const modalText = document.getElementById('modalFollowText');

            if (modalBtn) {
                if (isFollowing) modalBtn.classList.add('following');
                else modalBtn.classList.remove('following');
            }
            if (modalIcon) modalIcon.className = `fa-solid fa-${isFollowing ? 'user-check' : 'user-plus'}`;
            if (modalText) modalText.innerText = isFollowing ? 'Mengikuti' : 'Ikuti';
        }

        function toggleLike(e, postId) {
            if (e) e.stopPropagation();
            let likesData = JSON.parse(localStorage.getItem('post_likes_data') || '{}');
            if (!likesData[postId]) likesData[postId] = { count: 0, userLiked: false };

            if (likesData[postId].userLiked) {
                likesData[postId].count = Math.max(0, likesData[postId].count - 1);
                likesData[postId].userLiked = false;
            } else {
                likesData[postId].count += 1;
                likesData[postId].userLiked = true;
                spawnFloatingHeart(e);
            }

            localStorage.setItem('post_likes_data', JSON.stringify(likesData));
            syncLikeUI(postId);
        }

        function toggleLikeFromModal(e) {
            if (currentActivePostId) {
                toggleLike(e, currentActivePostId);
            }
        }

        function syncLikeUI(postId) {
            const likesData = JSON.parse(localStorage.getItem('post_likes_data') || '{}');
            const isLiked = likesData[postId] ? likesData[postId].userLiked : false;
            const count = likesData[postId] ? likesData[postId].count : 0;

            const syncSingleBtn = (elemId) => {
                const btn = document.getElementById(elemId);
                if (btn) {
                    const icon = btn.querySelector('i');
                    const countSpan = btn.querySelector('.like-count');
                    if (isLiked) {
                        btn.classList.add('liked');
                        if (icon) icon.className = 'fa-solid fa-heart';
                    } else {
                        btn.classList.remove('liked');
                        if (icon) icon.className = 'fa-regular fa-heart';
                    }
                    if (countSpan) countSpan.innerText = count;
                }
            };

            syncSingleBtn(`likeBtn_${postId}`);
            syncSingleBtn(`marketLikeBtn_${postId}`);

            if (currentActivePostId === postId) {
                const modalBtn = document.getElementById('modalLikeBtn');
                const modalIcon = document.getElementById('modalLikeIcon');
                const modalCount = document.getElementById('modalLikeCount');

                if (modalBtn) {
                    if (isLiked) modalBtn.classList.add('liked');
                    else modalBtn.classList.remove('liked');
                }
                if (modalIcon) modalIcon.className = `fa-${isLiked ? 'solid' : 'regular'} fa-heart`;
                if (modalCount) modalCount.innerText = count;
            }
        }

        function spawnFloatingHeart(e) {
            const heart = document.createElement('div');
            heart.className = 'floating-heart';
            heart.innerHTML = '<i class="fa-solid fa-heart"></i>';
            const x = e && e.clientX ? e.clientX : window.innerWidth / 2;
            const y = e && e.clientY ? e.clientY : window.innerHeight / 2;
            heart.style.left = `${x}px`;
            heart.style.top = `${y}px`;
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 1200);
        }

        /* ========================================================
           POST READING MODAL WITH TTS & MODERN COMMENTS
           ======================================================== */
        function openPostModal(postId, title, fullBody) {
            currentActivePostId = postId;
            resetCommentForm();
            stopSpeechReader();

            document.getElementById('modalTitle').innerText = title;
            const bodyEl = document.getElementById('modalBody');
            bodyEl.innerHTML = fullBody;
            bodyEl.style.fontSize = `${currentPostFontSize}px`;

            // Hitung estimasi waktu baca
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = fullBody;
            const textContent = tempDiv.textContent || tempDiv.innerText || '';
            const wordsCount = textContent.trim().split(/\s+/).length;
            const readMinutes = Math.max(1, Math.ceil(wordsCount / 180));
            document.getElementById('modalReadingTime').innerText = `${readMinutes} menit baca`;

            syncLikeUI(postId);
            syncFollowUI();
            loadModalComments(postId);

            document.getElementById('postModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closePostModal(e) {
            if (e.target.id === 'postModal') closePostModalForce();
        }

        function closePostModalForce() {
            stopSpeechReader();
            document.getElementById('postModal').classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        function zoomPostText(step) {
            currentPostFontSize = Math.min(Math.max(currentPostFontSize + (step * 1.5), 12), 22);
            const bodyEl = document.getElementById('modalBody');
            if (bodyEl) bodyEl.style.fontSize = `${currentPostFontSize}px`;
        }

        /* TEXT-TO-SPEECH (TTS) ENGINE */
        function toggleSpeechReader() {
            if (!('speechSynthesis' in window)) {
                showToast("Browser tidak mendukung fitur Text-to-Speech.", "info");
                return;
            }

            if (isSpeaking) {
                stopSpeechReader();
            } else {
                startSpeechReader();
            }
        }

        function startSpeechReader() {
            const title = document.getElementById('modalTitle').innerText;
            const bodyText = document.getElementById('modalBody').innerText;
            const fullText = `${title}. ${bodyText}`;

            window.speechSynthesis.cancel();
            const utterance = new SpeechSynthesisUtterance(fullText);
            utterance.lang = 'id-ID';
            utterance.rate = 1.0;

            utterance.onend = function() { stopSpeechReader(); };
            utterance.onerror = function() { stopSpeechReader(); };

            window.speechSynthesis.speak(utterance);
            isSpeaking = true;

            const icon = document.getElementById('ttsIcon');
            const label = document.getElementById('ttsLabel');
            if (icon) icon.className = 'fa-solid fa-circle-stop';
            if (label) label.innerText = 'Hentikan Suara';
            showToast("Memutar audio narasi artikel...", "info");
        }

        function stopSpeechReader() {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
            }
            isSpeaking = false;
            const icon = document.getElementById('ttsIcon');
            const label = document.getElementById('ttsLabel');
            if (icon) icon.className = 'fa-solid fa-volume-high';
            if (label) label.innerText = 'Dengarkan Artikel';
        }

        function shareToLovedOne() {
            const modalTitle = document.getElementById('modalTitle').innerText;
            const shareText = `Halo! Coba lihat artikel menarik ini: "${modalTitle}" ❤️\n`;
            const url = window.location.href;

            if (navigator.share) {
                navigator.share({ title: modalTitle, text: shareText, url: url }).catch(() => {});
            } else {
                navigator.clipboard.writeText(`${shareText}${url}`);
                showToast("Tautan artikel berhasil disalin!", "success");
            }
        }

        /* ========================================================
           MODERN COMMENT SYSTEM (FORMSPREE + LOCALSTORAGE)
           ======================================================== */
        function loadModalComments(postId) {
            const commentsData = JSON.parse(localStorage.getItem('post_comments_data') || '{}');
            const listContainer = document.getElementById('modalCommentsList');
            if (!listContainer) return;
            listContainer.innerHTML = '';

            const list = commentsData[postId] || [];
            if (list.length === 0) {
                listContainer.innerHTML = `<div style="font-size:0.78rem; color:var(--text-sub); text-align:center; padding:12px;">Belum ada komentar. Jadilah yang pertama memberikan tanggapan!</div>`;
                return;
            }

            list.forEach((c, idx) => {
                const initial = (c.name || 'A').charAt(0).toUpperCase();
                const item = document.createElement('div');
                item.className = 'comment-item';
                item.innerHTML = `
                    <div class="comment-header">
                        <div class="comment-author-box">
                            <div class="comment-avatar-initials">${initial}</div>
                            <div class="comment-author">${escapeHTML(c.name)}</div>
                        </div>
                        <div class="comment-actions">
                            <button class="comment-action-btn" onclick="prepareEditComment(${idx})" title="Edit Komentar"><i class="fa-regular fa-pen-to-square"></i></button>
                            <button class="comment-action-btn delete" onclick="deleteComment(${idx})" title="Hapus Komentar"><i class="fa-regular fa-trash-can"></i></button>
                        </div>
                    </div>
                    <div class="comment-text">${escapeHTML(c.text)}</div>
                    <div class="comment-time">${c.time} ${c.isEdited ? '(diedit)' : ''}</div>
                `;
                listContainer.appendChild(item);
            });
        }

        function addModalComment() {
            const nameInput = document.getElementById('commentName');
            const textInput = document.getElementById('commentText');

            const name = nameInput.value.trim() || 'Pengunjung Anonim';
            const text = textInput.value.trim();
            const postTitle = document.getElementById('modalTitle').innerText;

            if (!text) {
                showToast("Silakan tulis isi komentar terlebih dahulu.", "info");
                return;
            }

            let commentsData = JSON.parse(localStorage.getItem('post_comments_data') || '{}');
            if (!commentsData[currentActivePostId]) commentsData[currentActivePostId] = [];

            if (editingCommentIndex !== null) {
                commentsData[currentActivePostId][editingCommentIndex].name = name;
                commentsData[currentActivePostId][editingCommentIndex].text = text;
                commentsData[currentActivePostId][editingCommentIndex].isEdited = true;
                showToast("Perubahan komentar berhasil disimpan!", "success");
            } else {
                const newComment = {
                    name: name,
                    text: text,
                    time: new Date().toLocaleDateString('id-ID', { hour: '2-digit', minute: '2-digit' }),
                    isEdited: false
                };
                commentsData[currentActivePostId].unshift(newComment);
                showToast("Komentar Anda berhasil terkirim!", "success");
            }

            localStorage.setItem('post_comments_data', JSON.stringify(commentsData));

            // Formspree Integrasi Pengiriman Email
            if (FORMSPREE_ENDPOINT_ID && FORMSPREE_ENDPOINT_ID !== 'YOUR_FORMSPREE_ID') {
                fetch(`https://formspree.io/f/${FORMSPREE_ENDPOINT_ID}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        'Nama Pengirim': name,
                        'Isi Komentar': text,
                        'Judul Postingan': postTitle,
                        'Waktu': new Date().toLocaleString()
                    })
                }).catch(() => {});
            }

            resetCommentForm();
            loadModalComments(currentActivePostId);
            updateTotalCommentsCount();
        }

        function prepareEditComment(index) {
            const commentsData = JSON.parse(localStorage.getItem('post_comments_data') || '{}');
            const comment = commentsData[currentActivePostId][index];
            if (!comment) return;

            document.getElementById('commentName').value = comment.name;
            document.getElementById('commentText').value = comment.text;
            document.getElementById('commentSubmitBtn').innerText = 'Simpan';
            document.getElementById('cancelEditBtn').style.display = 'inline-block';

            editingCommentIndex = index;
            document.getElementById('commentText').focus();
        }

        function cancelCommentEdit() {
            resetCommentForm();
        }

        function deleteComment(index) {
            if (!confirm("Hapus komentar ini?")) return;

            let commentsData = JSON.parse(localStorage.getItem('post_comments_data') || '{}');
            if (commentsData[currentActivePostId]) {
                commentsData[currentActivePostId].splice(index, 1);
                localStorage.setItem('post_comments_data', JSON.stringify(commentsData));
            }

            if (editingCommentIndex === index) resetCommentForm();
            loadModalComments(currentActivePostId);
            updateTotalCommentsCount();
            showToast("Komentar telah dihapus.", "info");
        }

        function resetCommentForm() {
            document.getElementById('commentName').value = '';
            document.getElementById('commentText').value = '';
            document.getElementById('commentSubmitBtn').innerText = 'Kirim Komentar';
            const cancelBtn = document.getElementById('cancelEditBtn');
            if (cancelBtn) cancelBtn.style.display = 'none';
            editingCommentIndex = null;
        }

        function updateTotalCommentsCount() {
            const commentsData = JSON.parse(localStorage.getItem('post_comments_data') || '{}');
            let total = 0;
            Object.keys(commentsData).forEach(k => total += commentsData[k].length);
            const countEl = document.getElementById('totalComments');
            if (countEl) countEl.innerText = total;
        }

        /* ========================================================
           RECENT COMMENTS DIALOG MODAL (FEED + LOCAL SYNC)
           ======================================================== */
        function openRecentCommentsModal() {
            closeMenu();
            loadRecentCommentsModalFeed();
            document.getElementById('recentCommentsModal').classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        function closeRecentCommentsModal(e) {
            if (e.target.id === 'recentCommentsModal') closeRecentCommentsModalForce();
        }

        function closeRecentCommentsModalForce() {
            document.getElementById('recentCommentsModal').classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        function loadRecentCommentsModalFeed() {
            const container = document.getElementById('recentCommentsListModal');
            if (!container) return;

            fetch('/feeds/comments/default?alt=json&max-results=10')
                .then(res => res.json())
                .then(data => {
                    renderCommentsModalList(data);
                })
                .catch(() => {
                    renderCommentsModalList(null);
                });
        }

        function renderCommentsModalList(feedData) {
            const container = document.getElementById('recentCommentsListModal');
            if (!container) return;
            container.innerHTML = '';
            let recentItems = [];

            if (feedData && feedData.feed && feedData.feed.entry) {
                feedData.feed.entry.forEach(entry => {
                    const author = entry.author[0].name.$t;
                    const content = entry.summary ? entry.summary.$t : (entry.content ? entry.content.$t : '');
                    const tempDiv = document.createElement('div');
                    tempDiv.innerHTML = content;
                    const cleanText = tempDiv.textContent || tempDiv.innerText || '';

                    let postTitle = 'Postingan Blog';
                    let postId = '';

                    if (entry.link) {
                        entry.link.forEach(link => {
                            if (link.rel === 'alternate') {
                                postTitle = link.title || 'Lihat Postingan';
                                const match = link.href.match(/post-(\d+)/);
                                if (match) postId = match[1];
                            }
                        });
                    }

                    recentItems.push({
                        name: author,
                        text: cleanText.substring(0, 100) + (cleanText.length > 100 ? '...' : ''),
                        postTitle: postTitle,
                        postId: postId
                    });
                });
            }

            const localComments = JSON.parse(localStorage.getItem('post_comments_data') || '{}');
            Object.keys(localComments).forEach(pId => {
                const targetPost = allPostsData.find(p => p.postId === pId);
                const title = targetPost ? targetPost.title : 'Postingan Blog';

                localComments[pId].forEach(c => {
                    recentItems.unshift({
                        name: c.name,
                        text: c.text.substring(0, 100) + (c.text.length > 100 ? '...' : ''),
                        postTitle: title,
                        postId: pId
                    });
                });
            });

            if (recentItems.length === 0) {
                container.innerHTML = `<div style="text-align:center; font-size:0.8rem; color:var(--text-sub); padding:25px;">Belum ada komentar terbaru.</div>`;
                return;
            }

            recentItems.slice(0, 12).forEach(item => {
                const commentEl = document.createElement('div');
                commentEl.className = 'recent-dialog-item';
                
                commentEl.onclick = function() {
                    closeRecentCommentsModalForce();
                    const targetPost = allPostsData.find(p => p.postId === item.postId || p.title === item.postTitle);
                    if (targetPost) {
                        openPostModal(targetPost.postId, targetPost.title, targetPost.body);
                    } else {
                        showToast(`Membuka: ${item.postTitle}`, "info");
                    }
                };

                commentEl.innerHTML = `
                    <div class="recent-dialog-author">
                        <i class="fa-regular fa-circle-user"></i> ${escapeHTML(item.name)}
                    </div>
                    <div class="recent-dialog-text">"${escapeHTML(item.text)}"</div>
                    <div class="recent-dialog-post">
                        <i class="fa-solid fa-newspaper" style="color:var(--accent-color);"></i>
                        <span>Di: <b>${escapeHTML(item.postTitle)}</b></span>
                    </div>
                `;
                container.appendChild(commentEl);
            });
        }

        /* ========================================================
           WALLPAPER, THEMES, FONTS & CUSTOMIZATION
           ======================================================== */
        function setCustomBgColor(colorVal) {
            document.body.style.backgroundImage = 'none';
            document.body.style.backgroundColor = colorVal;
            localStorage.setItem('custom_bg_val', colorVal);
            showToast("Warna latar diperbarui", "success");
        }

        function setGradientBg(gradientStr) {
            document.body.style.backgroundImage = 'none';
            document.body.style.background = gradientStr;
            localStorage.setItem('custom_bg_val', gradientStr);
            showToast("Gradien latar diterapkan", "success");
        }

        function setBgUrlFromInput() {
            const url = document.getElementById('bgUrlInput').value.trim();
            if (!url) return;
            document.body.style.backgroundImage = `url('${url}')`;
            localStorage.setItem('custom_bg_val', url);
            showToast("Wallpaper URL diterapkan!", "success");
        }

        function handleBgFileUpload(event) {
            const file = event.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                const dataUrl = e.target.result;
                document.body.style.backgroundImage = `url('${dataUrl}')`;
                localStorage.setItem('custom_bg_val', dataUrl);
                showToast("Wallpaper galeri berhasil dipasang!", "success");
            };
            reader.readAsDataURL(file);
        }

        function resetCustomBg() {
            localStorage.removeItem('custom_bg_val');
            document.body.style.backgroundImage = 'none';
            const savedPreset = localStorage.getItem('themePreset') || 'default';
            applyThemePreset(savedPreset, false);
            showToast("Latar belakang di-reset ke tema default", "info");
        }

        function setGlassBlur(blurVal) {
            document.documentElement.style.setProperty('--glass-blur', blurVal);
            localStorage.setItem('glass_blur_val', blurVal);
            showToast(`Efek blur kaca: ${blurVal}`, "info");
        }

        function toggleBubbles() {
            isBubblesOn = !isBubblesOn;
            localStorage.setItem('bubbles_enabled', isBubblesOn);
            syncBubbleUI();
            setBgAnimation(isBubblesOn ? currentAnimType : 'none', true);
            showToast(isBubblesOn ? "Animasi efek jatuh diaktifkan" : "Animasi efek jatuh dimatikan", "info");
        }

        function syncBubbleUI() {
            const statusEl = document.getElementById('bubbleStatus');
            if (statusEl) {
                statusEl.innerText = isBubblesOn ? 'ON' : 'OFF';
                statusEl.style.color = isBubblesOn ? '#10b981' : 'var(--text-sub)';
            }
        }

        function setFontFamily(type, save = true) {
            let fontStack = "'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif";
            if (type === 'serif') fontStack = "Georgia, 'Times New Roman', Times, serif";
            else if (type === 'mono') fontStack = "'Fira Code', Consolas, 'Courier New', monospace";
            else if (type === 'cursive') fontStack = "'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', cursive";

            document.documentElement.style.setProperty('--main-font-family', fontStack);
            if (save) {
                localStorage.setItem('fontFamily', type);
                showToast(`Font disetel ke ${type.toUpperCase()}`, "info");
            }
        }

        function setFontSize(size) {
            document.documentElement.style.setProperty('--base-font-size', size);
            localStorage.setItem('fontSize', size);
            showToast(`Ukuran teks disetel ke ${size}`, "info");
        }

        function applyThemePreset(presetName, save = true) {
            document.body.classList.remove('theme-sakura', 'theme-cyberpunk', 'theme-emerald', 'theme-sunset', 'light-mode');
            if (presetName === 'sakura') document.body.classList.add('theme-sakura');
            else if (presetName === 'cyberpunk') document.body.classList.add('theme-cyberpunk');
            else if (presetName === 'emerald') document.body.classList.add('theme-emerald');
            else if (presetName === 'sunset') document.body.classList.add('theme-sunset');
            else if (presetName === 'light') document.body.classList.add('light-mode');

            if (save) {
                localStorage.setItem('themePreset', presetName);
                showToast(`Tema preset: ${presetName.toUpperCase()}`, "success");
            }
        }

        function toggleThemeMode() {
            const isLight = document.body.classList.contains('light-mode');
            applyThemePreset(isLight ? 'default' : 'light');
        }

        function toggleMenu() {
            const menu = document.getElementById('dropdownMenu');
            if (!menu) return;
            if (menu.classList.contains('active')) closeMenu();
            else {
                menu.classList.remove('closing');
                menu.classList.add('active');
            }
        }

        function closeMenu() {
            const menu = document.getElementById('dropdownMenu');
            if (menu && menu.classList.contains('active')) {
                menu.classList.remove('active');
                menu.classList.add('closing');
                setTimeout(() => menu.classList.remove('closing'), 300);
            }
        }

        window.addEventListener('click', function(e) {
            const menu = document.getElementById('dropdownMenu');
            const button = document.getElementById('menuToggle');
            if (menu && button && !menu.contains(e.target) && !button.contains(e.target)) {
                closeMenu();
            }
        });

        function updateClock() {
            const now = new Date();
            const clockEl = document.getElementById('liveClock');
            if (clockEl) clockEl.innerText = now.toLocaleTimeString('id-ID');
        }
        setInterval(updateClock, 1000);
        updateClock();

        /* AUDIO & PARTICLES */
        function toggleAmbientAudio() {
            const audio = document.getElementById('ambientAudio');
            const status = document.getElementById('audioStatus');
            if (!audio) return;

            if (audio.paused) {
                audio.play().then(() => {
                    if (status) {
                        status.innerText = 'PLAYING';
                        status.style.color = '#10b981';
                    }
                    showToast("Memutar audio santai Lofi", "info");
                }).catch(() => {
                    showToast("Izinkan browser memutar audio", "info");
                });
            } else {
                audio.pause();
                if (status) {
                    status.innerText = 'OFF';
                    status.style.color = 'var(--text-sub)';
                }
                showToast("Audio Lofi dijeda", "info");
            }
        }

        const particleIcons = { leaf: '🍃', snow: '❄️', star: '✨', heart: '❤️' };

        function setBgAnimation(type, save = true) {
            if (type !== 'none') currentAnimType = type;
            if (save && type !== 'none') localStorage.setItem('bgAnimType', type);

            clearInterval(particleInterval);
            document.querySelectorAll('.falling-particle').forEach(p => p.remove());

            if (type === 'none' || !isBubblesOn) return;

            particleInterval = setInterval(() => {
                const particle = document.createElement('div');
                particle.className = 'falling-particle';
                particle.innerText = particleIcons[type] || '✨';
                particle.style.left = Math.random() * 95 + 'vw';
                particle.style.animationDuration = (Math.random() * 3.5 + 2.5) + 's';
                particle.style.fontSize = (Math.random() * 12 + 14) + 'px';
                document.body.appendChild(particle);

                setTimeout(() => particle.remove(), 6000);
            }, particleSpeed);
        }

        /* STATS & REVEAL */
        function initLikesAndStats() {
            if (!localStorage.getItem('bg_views_all')) {
                localStorage.setItem('bg_views_all', '248');
                localStorage.setItem('bg_views_today', '14');
                localStorage.setItem('bg_views_yesterday', '21');
                localStorage.setItem('bg_views_month', '76');
                localStorage.setItem('bg_views_lastmonth', '172');
                localStorage.setItem('bg_base_followers', '10');
                localStorage.setItem('bg_total_followers', '10');
            } else {
                let currentViews = parseInt(localStorage.getItem('bg_views_all') || '200') + 1;
                let currentToday = parseInt(localStorage.getItem('bg_views_today') || '10') + 1;
                localStorage.setItem('bg_views_all', currentViews);
                localStorage.setItem('bg_views_today', currentToday);
            }

            const setTxt = (id, val) => {
                const el = document.getElementById(id);
                if (el) el.innerText = val;
            };

            setTxt('viewsAll', localStorage.getItem('bg_views_all'));
            setTxt('viewsToday', localStorage.getItem('bg_views_today'));
            setTxt('viewsYesterday', localStorage.getItem('bg_views_yesterday'));
            setTxt('viewsMonth', localStorage.getItem('bg_views_month'));
            setTxt('viewsLastMonth', localStorage.getItem('bg_views_lastmonth'));
            setTxt('totalFollowers', localStorage.getItem('bg_total_followers') || '10');
        }

        function initScrollReveal() {
            const revealElements = document.querySelectorAll(".scroll-reveal");
            const revealObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("revealed");
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.08 });
            revealElements.forEach(el => revealObserver.observe(el));
        }

        /* TYPING EFFECT */
        const words = ["Fullstack Developer", "IT Support Specialist", "Hardware Overclocker", "Creative Content Creator"];
        let wordIdx = 0;

        function typingEffect() {
            let word = words[wordIdx].split("");
            var loopTyping = function() {
                if (word.length > 0) {
                    const el = document.getElementById('typingText');
                    if (el) el.innerHTML += word.shift();
                } else {
                    setTimeout(deletingEffect, 2000);
                    return false;
                }
                setTimeout(loopTyping, 90);
            };
            loopTyping();
        }

        function deletingEffect() {
            let word = words[wordIdx].split("");
            var loopDeleting = function() {
                if (word.length > 0) {
                    word.pop();
                    const el = document.getElementById('typingText');
                    if (el) el.innerHTML = word.join("");
                } else {
                    wordIdx = (words.length > (wordIdx + 1)) ? wordIdx + 1 : 0;
                    setTimeout(typingEffect, 400);
                    return false;
                }
                setTimeout(loopDeleting, 45);
            };
            loopDeleting();
        }

        typingEffect();

        /* TOAST & UTILITIES */
        function showToast(msg, type = "info") {
            const container = document.getElementById('toastContainer');
            if (!container) return;

            const toast = document.createElement('div');
            toast.className = 'toast-msg';
            const icon = type === 'success' ? 'fa-circle-check' : 'fa-circle-info';
            toast.innerHTML = `<i class="fa-solid ${icon}" style="color:var(--accent-color);"></i> <span>${escapeHTML(msg)}</span>`;
            
            container.appendChild(toast);
            setTimeout(() => {
                toast.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
                toast.style.opacity = '0';
                toast.style.transform = 'translateY(10px)';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }

        function copyEmail() {
            navigator.clipboard.writeText("gandzar@gmail.com");
            showToast("Alamat email gandzar@gmail.com berhasil disalin!", "success");
        }

        function shareProfile() {
            if (navigator.share) {
                navigator.share({
                    title: document.title,
                    text: 'Kunjungi blog portofolio & software Gandzar Subagja',
                    url: window.location.href
                }).catch(() => {});
            } else {
                navigator.clipboard.writeText(window.location.href);
                showToast("Tautan blog berhasil disalin ke clipboard!", "success");
            }
        }

        function escapeHTML(str) {
            if (!str) return '';
            return String(str).replace(/[&<>'"]/g, 
                tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
            );
        }

        /* TOUCH RIPPLE RING */
        window.addEventListener('click', (e) => {
            const container = document.getElementById('touchContainer');
            if (!container) return;
            const ring = document.createElement('div');
            ring.className = 'touch-ring';
            ring.style.left = `${e.clientX}px`;
            ring.style.top = `${e.clientY}px`;
            container.appendChild(ring);
            setTimeout(() => ring.remove(), 700);
        });
      //]]>
    </script>
  </body>
</html>
'''

def main():
    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public", "merged_blog_theme.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(XML_CONTENT)
    print(f"Successfully generated merged XML theme to: {out_path}")
    print(f"Total size: {os.path.getsize(out_path)} bytes")

if __name__ == "__main__":
    main()
