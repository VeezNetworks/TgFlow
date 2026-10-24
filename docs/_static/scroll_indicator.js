document.addEventListener("DOMContentLoaded", () => {
  const rail = document.createElement("div");
  rail.className = "tgflow-scroll-rail";
  
  const track = document.createElement("div");
  track.className = "tgflow-scroll-track";

  const thumb = document.createElement("div");
  thumb.className = "tgflow-scroll-thumb";

  track.appendChild(thumb);

  for (let i = 0; i < 18; i++) {
    const tick = document.createElement("div");
    tick.className = "tgflow-scroll-tick";
    tick.style.top = `${(i / 17) * 100}%`;
    track.appendChild(tick);
  }

  rail.appendChild(track);
  document.body.appendChild(rail);

  let isDragging = false;

  const updateThumb = () => {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (scrollHeight <= 0) return;

    const progress = Math.min(Math.max(scrollTop / scrollHeight, 0), 1);
    const trackHeight = track.clientHeight - thumb.clientHeight;
    const thumbTop = progress * trackHeight;
    thumb.style.transform = `translateY(${thumbTop}px)`;
  };

  window.addEventListener("scroll", updateThumb, { passive: true });
  window.addEventListener("resize", updateThumb);
  updateThumb();

  track.addEventListener("click", (e) => {
    const rect = track.getBoundingClientRect();
    const clickY = e.clientY - rect.top;
    const progress = Math.min(Math.max(clickY / rect.height, 0), 1);
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    window.scrollTo({
      top: progress * scrollHeight,
      behavior: "smooth"
    });
  });

  const setupTocScrollspy = () => {
    const tocLinks = document.querySelectorAll(".toc-tree a");
    if (!tocLinks.length) return;

    const headings = [];
    tocLinks.forEach((link) => {
      const href = link.getAttribute("href");
      if (href && href.startsWith("#")) {
        const target = document.querySelector(href);
        if (target) {
          headings.push({ link, target });
        }
      }
    });

    const highlightToc = () => {
      const scrollPos = window.scrollY + 120;
      let activeItem = null;

      for (let i = 0; i < headings.length; i++) {
        if (headings[i].target.offsetTop <= scrollPos) {
          activeItem = headings[i].link;
        } else {
          break;
        }
      }

      tocLinks.forEach((l) => l.classList.remove("tgflow-toc-active"));
      if (activeItem) {
        activeItem.classList.add("tgflow-toc-active");
      }
    };

    window.addEventListener("scroll", highlightToc, { passive: true });
    highlightToc();
  };

  setupTocScrollspy();
});
