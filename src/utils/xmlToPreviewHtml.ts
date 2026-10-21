/**
 * Converts Blogger XML template into a previewable HTML document
 * suitable for iframe srcDoc in the Live Simulator.
 */
export function convertXmlToPreviewHtml(xml: string, titleOverride?: string): string {
  let html = xml;

  // Remove XML declaration
  html = html.replace(/<\?xml[^>]*\?>/g, '');

  // Standardize html tag
  html = html.replace(/<html[^>]*>/, '<!DOCTYPE html><html lang="id">');

  // Replace b:skin with standard <style> tag
  html = html.replace(/<b:skin><!\[CDATA\[/g, '<style>');
  html = html.replace(/\]\]><\/b:skin>/g, '</style>');

  // Replace title placeholder
  const displayTitle = titleOverride || 'Gandzar Subagja - Official Blog & Portfolio';
  html = html.replace(/<data:view\.title\.escaped\/>/g, displayTitle);
  html = html.replace(/<data:blog\.title\.escaped\/>/g, displayTitle);
  html = html.replace(/<data:view\.description\.escaped\/>/g, 'Official Blog, Downloader & Tech Articles');
  html = html.replace(/<data:blog\.canonicalUrl\/>/g, 'https://bagja.dev');
  html = html.replace(/<data:blog\.canonicalHomepageUrl\/>/g, 'https://bagja.dev');

  // Remove Blogger head include
  html = html.replace(/<b:include[^>]*all-head-content[^>]*\/>/g, '');

  // Handle 404 conditional (keep standard content for preview)
  html = html.replace(/<b:if cond=['"]data:view\.isError['"]>[\s\S]*?<\/b:if>\s*<b:else\/>/g, '');
  html = html.replace(/<\/b:else>/g, '');
  html = html.replace(/<\/b:if>/g, '');

  // Replace Blogger sections and widgets
  html = html.replace(/<b:section[^>]*>/g, '<div class="blogger-section-wrapper">');
  html = html.replace(/<\/b:section>/g, '</div>');
  html = html.replace(/<b:widget[^>]*>/g, '<div class="blogger-widget-wrapper">');
  html = html.replace(/<\/b:widget>/g, '</div>');
  html = html.replace(/<b:includable[^>]*>/g, '<div class="blogger-includable-wrapper">');
  html = html.replace(/<\/b:includable>/g, '</div>');
  html = html.replace(/<b:loop[^>]*>/g, '');
  html = html.replace(/<\/b:loop>/g, '');

  // Clean attributes
  html = html.replace(/expr:href=['"][^'"]*['"]/g, 'href="#"');
  html = html.replace(/expr:content=['"][^'"]*['"]/g, 'content="Gandzar Subagja"');
  html = html.replace(/<data:post\.title\/>/g, 'Post Title');

  // Clean JS CDATA comments
  html = html.replace(/\/\/<!\[CDATA\[/g, '');
  html = html.replace(/\/\/\]\]>/g, '');

  return html;
}
