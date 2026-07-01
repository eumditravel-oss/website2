/**
 * main.js - Vanilla JS interactions for Sinyoung SCM Clone
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Header
  const header = document.querySelector('.header');
  const floatingTop = document.querySelector('.floating-top');
  
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('sticky');
    } else {
      header.classList.remove('sticky');
    }

    // Top button visibility
    if (window.scrollY > 300) {
      floatingTop.classList.add('visible');
    } else {
      floatingTop.classList.remove('visible');
    }
  });

  // Top button click
  floatingTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // 2. Hero Slider (Vanilla JS Auto-rolling)
  const heroTrack = document.querySelector('.hero-slider');
  const dots = document.querySelectorAll('.dot');
  let currentSlide = 0;
  const totalSlides = dots.length;
  let slideInterval;

  function goToSlide(index) {
    currentSlide = index;
    heroTrack.style.transform = `translateX(-${currentSlide * 33.333}%)`;
    
    // Update dots
    dots.forEach(dot => dot.classList.remove('active'));
    dots[currentSlide].classList.add('active');
  }

  function nextSlide() {
    let next = currentSlide + 1;
    if (next >= totalSlides) next = 0;
    goToSlide(next);
  }

  // Dot click events
  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      goToSlide(index);
      resetInterval();
    });
  });

  // Auto slide
  function startInterval() {
    slideInterval = setInterval(nextSlide, 5000);
  }

  function resetInterval() {
    clearInterval(slideInterval);
    startInterval();
  }

  startInterval(); // Initialize auto rolling

  // 3. Project History Slider
  const historyTrack = document.querySelector('.history-track');
  const prevBtn = document.querySelector('.history-prev');
  const nextBtn = document.querySelector('.history-next');
  const historyItems = document.querySelectorAll('.history-item');
  
  let historyIndex = 0;

  function updateHistorySlider() {
    // Assuming 4 items visible on PC (25% width each)
    // We get the width of one item + gap
    if (historyItems.length === 0) return;
    const itemWidth = historyItems[0].offsetWidth + 20; // 20 is gap
    historyTrack.style.transform = `translateX(-${historyIndex * itemWidth}px)`;
  }

  if (nextBtn && prevBtn) {
    nextBtn.addEventListener('click', () => {
      // Don't scroll past the end
      if (historyIndex < historyItems.length - 4) { // 4 visible
        historyIndex++;
        updateHistorySlider();
      }
    });

    prevBtn.addEventListener('click', () => {
      if (historyIndex > 0) {
        historyIndex--;
        updateHistorySlider();
      }
    });

    // Handle window resize for accurate slide width
    window.addEventListener('resize', updateHistorySlider);
  }
});
