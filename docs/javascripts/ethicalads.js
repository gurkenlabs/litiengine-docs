/**
 * EthicalAds Integration for LITIENGINE Documentation (Zensical)
 * Privacy-preserving developer ads with instant navigation, staging support, and timeout fallbacks.
 */
(function() {
  // Global error listener to silently hide any blocked or failed ad images / pixels
  window.addEventListener('error', function(event) {
    const target = event.target;
    if (target && target.tagName === 'IMG' && target.closest('[data-ea-publisher], .ea-sidebar-wrapper, .ethical-ad-article-wrapper')) {
      target.style.display = 'none';
    }
  }, true);

  function setupAds() {
    const hostname = window.location.hostname;
    // On localhost or staging domains (such as github.io), request test ads so EthicalAds doesn't fail domain checks
    const isTestEnv = hostname === 'localhost' || 
                      hostname === '127.0.0.1' || 
                      hostname.endsWith('github.io') || 
                      hostname.endsWith('.dev') ||
                      hostname.includes('preview');
    const testAttr = isTestEnv ? ' data-ea-test="true"' : '';

    // 1. Table of Contents Sidebar Placement (Desktop)
    const tocNav = document.querySelector('.md-sidebar--secondary nav.md-nav--secondary');
    if (tocNav) {
      let adSidebarWrapper = document.getElementById('ea-sidebar-container');
      if (!adSidebarWrapper) {
        adSidebarWrapper = document.createElement('div');
        adSidebarWrapper.id = 'ea-sidebar-container';
        adSidebarWrapper.className = 'ea-sidebar-wrapper';
        tocNav.appendChild(adSidebarWrapper);
      }
      adSidebarWrapper.style.display = '';
      adSidebarWrapper.innerHTML = `<div data-ea-publisher="litiengine" data-ea-type="text"${testAttr} class="adaptive bordered"></div>`;
    }

    // 2. Article Bottom Placement (Mobile / No-sidebar view)
    const contentInner = document.querySelector('.md-content__inner article') || document.querySelector('.md-content__inner');
    if (contentInner) {
      let adArticleWrapper = document.getElementById('ea-article-container');
      if (!adArticleWrapper) {
        adArticleWrapper = document.createElement('div');
        adArticleWrapper.id = 'ea-article-container';
        adArticleWrapper.className = 'ethical-ad-article-wrapper';
        contentInner.appendChild(adArticleWrapper);
      }
      adArticleWrapper.style.display = '';
      adArticleWrapper.innerHTML = `<div data-ea-publisher="litiengine" data-ea-type="image"${testAttr} class="adaptive bordered"></div>`;
    }

    // 3. Trigger EthicalAds reload with retry and timeout guard
    function triggerAds(attempts = 0) {
      if (window.ethicalads && typeof window.ethicalads.load === 'function') {
        try {
          window.ethicalads.load();
        } catch (e) {
          console.debug('EthicalAds load error', e);
        }
      } else if (attempts < 6) {
        setTimeout(() => triggerAds(attempts + 1), 250);
      }
    }
    triggerAds();

    // 4. Timeout fallback: if ads are blocked or empty after 3.5 seconds, hide containers to prevent perpetual empty states
    setTimeout(function() {
      const adElements = document.querySelectorAll('[data-ea-publisher]');
      adElements.forEach(function(el) {
        // If ad element has not rendered any content or has ea-empty class
        if (el.classList.contains('ea-empty') || (!el.classList.contains('loaded') && !el.classList.contains('ea-loaded') && el.children.length === 0)) {
          const parentWrapper = el.closest('.ea-sidebar-wrapper, .ethical-ad-article-wrapper');
          if (parentWrapper) {
            parentWrapper.style.display = 'none';
          }
        }
      });
    }, 3500);
  }

  // Hook into Material/Zensical document observable stream if present
  if (typeof document$ !== 'undefined') {
    document$.subscribe(setupAds);
  } else {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', setupAds);
    } else {
      setupAds();
    }
  }

  // Backup observer for dynamic route changes
  window.addEventListener('popstate', setupAds);
  document.addEventListener('DOMContentSwitch', setupAds);
  window.addEventListener('load', setupAds);
})();
