/**
 * LITIENGINE Docs - Accessibility & Client-Side Enhancements
 * 
 * Hardens ARIA attributes for comboboxes, icon-only buttons, code annotations,
 * and decorative code line anchors for assistive technologies, AI agents, and Lighthouse audits.
 */
(function () {
  'use strict';

  function enhanceAccessibility() {
    // 1. Ensure code line number anchors are decorative for screen readers
    var codeAnchors = document.querySelectorAll('pre > code a[id^="__codelineno"], .linenodiv a');
    for (var i = 0; i < codeAnchors.length; i++) {
      var anchor = codeAnchors[i];
      if (!anchor.hasAttribute('aria-hidden')) {
        anchor.setAttribute('aria-hidden', 'true');
      }
      if (!anchor.hasAttribute('tabindex')) {
        anchor.setAttribute('tabindex', '-1');
      }
    }

    // 2. Fix search combobox missing required ARIA attributes
    var comboboxes = document.querySelectorAll('input[role="combobox"]');
    for (var j = 0; j < comboboxes.length; j++) {
      var input = comboboxes[j];
      if (!input.hasAttribute('aria-expanded')) {
        input.setAttribute('aria-expanded', 'false');
      }
      if (!input.hasAttribute('aria-haspopup')) {
        input.setAttribute('aria-haspopup', 'listbox');
      }
      if (!input.hasAttribute('aria-controls')) {
        input.setAttribute('aria-controls', 'search-results');
      }
    }

    // 3. Ensure buttons without text or labels have accessible names
    var buttons = document.querySelectorAll('button:not([aria-label]):not([title])');
    for (var k = 0; k < buttons.length; k++) {
      var btn = buttons[k];
      var text = (btn.textContent || '').trim();
      if (!text) {
        if (btn.classList.contains('r') || btn.closest('.md-search')) {
          if (btn.previousElementSibling === null) {
            btn.setAttribute('aria-label', 'Close search');
          } else {
            btn.setAttribute('aria-label', 'Filter search results');
          }
        } else if (btn.dataset && btn.dataset.mdComponent === 'search-reset') {
          btn.setAttribute('aria-label', 'Clear search');
        } else {
          btn.setAttribute('aria-label', 'Action');
        }
      }
    }

    // 4. Ensure code annotation links have discernible accessible text
    var annotations = document.querySelectorAll('a.md-annotation__index');
    for (var a = 0; a < annotations.length; a++) {
      var ann = annotations[a];
      if (!ann.getAttribute('aria-label')) {
        var match = (ann.getAttribute('href') || '').match(/annotation_(\d+)/);
        var num = match ? match[1] : (a + 1);
        ann.setAttribute('aria-label', 'Code annotation ' + num);
      }
    }
  }

  // Run on initial DOM content loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', enhanceAccessibility);
  } else {
    enhanceAccessibility();
  }

  // Observe dynamically mounted elements (e.g. search overlay, instant navigation)
  if (typeof MutationObserver !== 'undefined') {
    var observer = new MutationObserver(function () {
      enhanceAccessibility();
    });
    observer.observe(document.documentElement, {
      childList: true,
      subtree: true
    });
  }
})();
