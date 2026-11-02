/**
 * ==============================================================================
 * FLORAL FLIRTSS - JAVASCRIPT APPLICATION
 * Handmade Floral Gifting Boutique • Hyderabad, Telangana, India
 * ==============================================================================
 */

// 1. BUSINESS WHATSAPP CONFIGURATION (Stored once as required)
const WHATSAPP_NUMBER = "919542115708";

// Reference photo hosting (Cloudinary, free plan).
// 1) Create a free account at cloudinary.com  2) Settings > Upload > add an UNSIGNED upload preset
// 3) Paste your cloud name and preset name below.
const CLOUDINARY_CLOUD_NAME = "g1n4x1gg";
const CLOUDINARY_UPLOAD_PRESET = "floral_flirts_customer_upload";


// Google Analytics event helper (safe if GA is blocked)
function trackEvent(name, params) {
  try { if (typeof gtag === "function") gtag("event", name, params || {}); } catch (e) {}
}

async function uploadReferencePhoto(file) {
  const fd = new FormData();
  fd.append("file", file);
  fd.append("upload_preset", CLOUDINARY_UPLOAD_PRESET);
  const res = await fetch(`https://api.cloudinary.com/v1_1/${CLOUDINARY_CLOUD_NAME}/image/upload`, {
    method: "POST",
    body: fd
  });
  if (!res.ok) throw new Error("Upload failed");
  const data = await res.json();
  return data.secure_url;
}

/**
 * Generates an accessible, URL-encoded WhatsApp click-to-chat URL.
 * @param {string} message - Plaintext multiline message.
 * @returns {string} Fully encoded wa.me URL.
 */
function createWhatsAppUrl(message) {
  return `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
}

/**
 * Standard confirmation clause required for all booking enquiries.
 */
const CLOSING_CONFIRMATION_LINE = "Please confirm the final price, availability and delivery details before booking.";

document.addEventListener("DOMContentLoaded", () => {
  // Initialize all interactive modules
  initDateConstraints();
  initStickyHeader();
  initMobileDrawer();
  initScrollSpy();
  initScrollReveals();
  initLiveSummary();
  initReferencePhotos();
  initCustomBouquetForm();
  initProductEnquiries();
  initGeneralOrderButtons();
  initBackToTop();
});

/* --------------------------------------------------------------------------
   2. DATE PICKER CONSTRAINTS (Prevent Past Dates)
   -------------------------------------------------------------------------- */
function getTodayDateString() {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, "0");
  const day = String(now.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

function initDateConstraints() {
  const deliveryDateInput = document.getElementById("deliveryDate");
  if (!deliveryDateInput) return;

  const todayStr = getTodayDateString();
  // Set minimum date attribute to today's date in local time
  deliveryDateInput.min = todayStr;
}

/* --------------------------------------------------------------------------
   3. STICKY HEADER WITH SOFT SCROLLED BACKGROUND
   -------------------------------------------------------------------------- */
function initStickyHeader() {
  const header = document.getElementById("siteHeader");
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 40) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  };

  window.addEventListener("scroll", handleScroll, { passive: true });
  handleScroll(); // Initial check on page load
}

/* --------------------------------------------------------------------------
   4. ACCESSIBLE MOBILE NAVIGATION DRAWER
   -------------------------------------------------------------------------- */
function initMobileDrawer() {
  const toggleBtn = document.getElementById("mobileToggle");
  const closeBtn = document.getElementById("drawerClose");
  const drawer = document.getElementById("mobileDrawer");
  const backdrop = document.getElementById("mobileBackdrop");
  const drawerLinks = document.querySelectorAll(".drawer-link, .drawer-action-btn");

  if (!toggleBtn || !drawer || !backdrop) return;

  const openDrawer = () => {
    drawer.classList.add("open");
    backdrop.classList.add("open");
    drawer.setAttribute("aria-hidden", "false");
    toggleBtn.setAttribute("aria-expanded", "true");
    document.body.style.overflow = "hidden";
    if (closeBtn) closeBtn.focus();
  };

  const closeDrawer = () => {
    drawer.classList.remove("open");
    backdrop.classList.remove("open");
    drawer.setAttribute("aria-hidden", "true");
    toggleBtn.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
    toggleBtn.focus();
  };

  toggleBtn.addEventListener("click", openDrawer);
  if (closeBtn) closeBtn.addEventListener("click", closeDrawer);
  backdrop.addEventListener("click", closeDrawer);

  // Close drawer when any internal navigation link is tapped
  drawerLinks.forEach((link) => {
    link.addEventListener("click", () => {
      closeDrawer();
    });
  });

  // Close on Escape key press
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && drawer.classList.contains("open")) {
      closeDrawer();
    }
  });
}

/* --------------------------------------------------------------------------
   5. NAVIGATION SCROLL SPY (Active Link Highlighting)
   -------------------------------------------------------------------------- */
function initScrollSpy() {
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".nav-link");

  if (!sections.length || !navLinks.length) return;

  const observerOptions = {
    root: null,
    rootMargin: "-25% 0px -65% 0px",
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute("id");
        navLinks.forEach((link) => {
          const href = link.getAttribute("href");
          if (href === `#${id}`) {
            link.classList.add("active");
          } else {
            link.classList.remove("active");
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach((section) => observer.observe(section));
}

/* --------------------------------------------------------------------------
   6. RESTRAINED SCROLL REVEAL ANIMATIONS
   -------------------------------------------------------------------------- */
function initScrollReveals() {
  const reveals = document.querySelectorAll(".reveal-on-scroll");
  if (!reveals.length) return;

  // If user prefers reduced motion, reveal immediately
  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (prefersReducedMotion) {
    reveals.forEach((el) => el.classList.add("revealed"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("revealed");
          obs.unobserve(entry.target);
        }
      });
    },
    {
      rootMargin: "0px 0px -50px 0px",
      threshold: 0.1
    }
  );

  reveals.forEach((el) => observer.observe(el));
}

/* --------------------------------------------------------------------------
   7. LIVE BOUQUET SUMMARY ASIDE
   -------------------------------------------------------------------------- */
function initLiveSummary() {
  const flowerTypeSelect = document.getElementById("flowerType");
  const preferredColourSelect = document.getElementById("preferredColour");
  const bouquetSizeSelect = document.getElementById("bouquetSize");
  const occasionSelect = document.getElementById("occasion");
  const deliveryDateInput = document.getElementById("deliveryDate");
  const deliveryAreaInput = document.getElementById("deliveryArea");

  const summaryFlowerType = document.getElementById("summaryFlowerType");
  const summaryColour = document.getElementById("summaryColour");
  const summarySize = document.getElementById("summarySize");
  const summaryOccasion = document.getElementById("summaryOccasion");
  const summaryDate = document.getElementById("summaryDate");
  const summaryArea = document.getElementById("summaryArea");

  if (!flowerTypeSelect || !summaryFlowerType) return;

  const updateSummary = () => {
    if (summaryFlowerType) summaryFlowerType.textContent = flowerTypeSelect.value;
    if (summaryColour) summaryColour.textContent = preferredColourSelect.value;
    if (summarySize) summarySize.textContent = bouquetSizeSelect.value;
    if (summaryOccasion) summaryOccasion.textContent = occasionSelect.value;

    if (summaryDate) {
      if (deliveryDateInput.value) {
        summaryDate.textContent = deliveryDateInput.value;
      } else {
        summaryDate.textContent = "Not selected yet";
      }
    }

    if (summaryArea) {
      const areaVal = deliveryAreaInput.value.trim();
      summaryArea.textContent = areaVal ? areaVal : "Hyderabad";
    }
  };

  [flowerTypeSelect, preferredColourSelect, bouquetSizeSelect, occasionSelect, deliveryDateInput].forEach((el) => {
    el.addEventListener("change", updateSummary);
  });

  deliveryAreaInput.addEventListener("input", updateSummary);
  updateSummary(); // Initial sync
}

/* --------------------------------------------------------------------------
   8. CUSTOM BOUQUET FORM VALIDATION & WHATSAPP INTEGRATION
   -------------------------------------------------------------------------- */
const MAX_PHOTOS = 3;
const MAX_PHOTO_BYTES = 5 * 1024 * 1024;
let referencePhotoFiles = [];

function initReferencePhotos() {
  const input = document.getElementById("referencePhotos");
  const dropzone = document.getElementById("photoDropzone");
  const list = document.getElementById("photoPreviewList");
  const errorEl = document.getElementById("photoError");
  const summaryPhotos = document.getElementById("summaryPhotos");
  if (!input || !list) return;

  const render = () => {
    list.innerHTML = "";
    referencePhotoFiles.forEach((file, idx) => {
      const li = document.createElement("li");
      li.className = "photo-preview-item";
      const img = document.createElement("img");
      const url = URL.createObjectURL(file);
      img.src = url;
      img.alt = `Reference photo ${idx + 1}`;
      img.onload = () => URL.revokeObjectURL(url);
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "photo-remove-btn";
      btn.setAttribute("aria-label", `Remove reference photo ${idx + 1}`);
      btn.textContent = "\u00D7";
      btn.addEventListener("click", () => {
        referencePhotoFiles.splice(idx, 1);
        errorEl.textContent = "";
        render();
      });
      li.append(img, btn);
      list.appendChild(li);
    });
    if (summaryPhotos) {
      const n = referencePhotoFiles.length;
      summaryPhotos.textContent = n ? `${n} photo${n > 1 ? "s" : ""} added` : "None added";
    }
  };

  const addFiles = (fileList) => {
    errorEl.textContent = "";
    const problems = [];
    Array.from(fileList).forEach((file) => {
      if (!file.type.startsWith("image/")) {
        problems.push(`"${file.name}" is not an image.`);
      } else if (file.size > MAX_PHOTO_BYTES) {
        problems.push(`"${file.name}" is larger than 5 MB.`);
      } else if (referencePhotoFiles.length >= MAX_PHOTOS) {
        if (!problems.some((p) => p.startsWith("You can add"))) {
          problems.push(`You can add up to ${MAX_PHOTOS} photos.`);
        }
      } else {
        referencePhotoFiles.push(file);
      }
    });
    if (problems.length) errorEl.textContent = problems.join(" ");
    input.value = "";
    render();
  };

  input.addEventListener("change", () => addFiles(input.files));

  if (dropzone) {
    ["dragenter", "dragover"].forEach((evt) =>
      dropzone.addEventListener(evt, (e) => { e.preventDefault(); dropzone.classList.add("dragover"); })
    );
    ["dragleave", "drop"].forEach((evt) =>
      dropzone.addEventListener(evt, (e) => { e.preventDefault(); dropzone.classList.remove("dragover"); })
    );
    dropzone.addEventListener("drop", (e) => {
      if (e.dataTransfer && e.dataTransfer.files) addFiles(e.dataTransfer.files);
    });
  }

  const form = document.getElementById("customBouquetForm");
  if (form) {
    form.addEventListener("reset", () => {
      referencePhotoFiles = [];
      errorEl.textContent = "";
      render();
    });
  }
  render();
}

function initCustomBouquetForm() {
  const form = document.getElementById("customBouquetForm");
  if (!form) return;

  const nameInput = document.getElementById("customerName");
  const flowerTypeSelect = document.getElementById("flowerType");
  const preferredColourSelect = document.getElementById("preferredColour");
  const bouquetSizeSelect = document.getElementById("bouquetSize");
  const occasionSelect = document.getElementById("occasion");
  const dateInput = document.getElementById("deliveryDate");
  const areaInput = document.getElementById("deliveryArea");
  const messageInput = document.getElementById("giftMessage");
  const reqsInput = document.getElementById("additionalRequirements");

  const nameError = document.getElementById("nameError");
  const dateError = document.getElementById("dateError");
  const areaError = document.getElementById("areaError");
  const alertBox = document.getElementById("formAlertBox");

  const clearFieldError = (input, errorEl) => {
    input.classList.remove("input-error");
    input.removeAttribute("aria-invalid");
    if (errorEl) errorEl.textContent = "";
  };

  const setFieldError = (input, errorEl, message) => {
    input.classList.add("input-error");
    input.setAttribute("aria-invalid", "true");
    if (errorEl) errorEl.textContent = message;
  };

  // Live error clearing when typing or changing
  nameInput.addEventListener("input", () => clearFieldError(nameInput, nameError));
  dateInput.addEventListener("change", () => clearFieldError(dateInput, dateError));
  areaInput.addEventListener("input", () => clearFieldError(areaInput, areaError));

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    let hasErrors = false;
    const errorList = [];

    // Reset previous alert state
    alertBox.hidden = true;
    alertBox.textContent = "";
    clearFieldError(nameInput, nameError);
    clearFieldError(dateInput, dateError);
    clearFieldError(areaInput, areaError);

    // 1. Validate Customer Name (Required, reject whitespace only)
    const nameVal = nameInput.value.trim();
    if (!nameVal || nameVal.length < 2) {
      hasErrors = true;
      setFieldError(nameInput, nameError, "Please enter your name (at least 2 characters).");
      errorList.push("Your Name is required.");
    }

    // 2. Validate Delivery Date (Required, reject past dates)
    const dateVal = dateInput.value;
    const todayStr = getTodayDateString();

    if (!dateVal) {
      hasErrors = true;
      setFieldError(dateInput, dateError, "Please select your preferred delivery date.");
      errorList.push("Preferred Delivery Date is required.");
    } else if (dateVal < todayStr) {
      hasErrors = true;
      setFieldError(dateInput, dateError, "Delivery date cannot be in the past. Please choose today or a future date.");
      errorList.push("Delivery date cannot be in the past.");
    }

    // 3. Validate Delivery Area (Required, reject whitespace only)
    const areaVal = areaInput.value.trim();
    if (!areaVal || areaVal.length < 3) {
      hasErrors = true;
      setFieldError(areaInput, areaError, "Please specify your locality in Hyderabad (e.g. Jubilee Hills).");
      errorList.push("Delivery Area / Locality is required.");
    }

    // If validation fails, announce in alert box and focus the first invalid field
    if (hasErrors) {
      alertBox.textContent = `Please correct the following: ${errorList.join(" • ")}`;
      alertBox.hidden = false;

      const firstError = form.querySelector(".input-error");
      if (firstError) {
        firstError.focus();
      }
      return;
    }

    // Validation Succeeded
    const flowerTypeVal = flowerTypeSelect.value;
    const colourVal = preferredColourSelect.value;
    const sizeVal = bouquetSizeSelect.value;
    const occasionVal = occasionSelect.value;
    const giftMsgVal = messageInput.value.trim() || "None";
    const reqsVal = reqsInput.value.trim() || "None";

    // Open the WhatsApp tab right away (keeps popup blockers happy), fill it in after uploads finish
    const waWindow = window.open("", "_blank");
    const submitBtn = document.getElementById("submitEnquiryBtn");
    const btnLabel = submitBtn ? submitBtn.querySelector("span") : null;
    const originalLabel = btnLabel ? btnLabel.textContent : "";

    let photoLinks = [];
    let photoNote = "None";
    const hostingReady = CLOUDINARY_CLOUD_NAME && CLOUDINARY_UPLOAD_PRESET;

    if (referencePhotoFiles.length) {
      if (hostingReady) {
        if (submitBtn) submitBtn.disabled = true;
        if (btnLabel) btnLabel.textContent = "Uploading photos…";
        try {
          photoLinks = await Promise.all(referencePhotoFiles.map(uploadReferencePhoto));
          photoNote = photoLinks.map((url, i) => `\n   ${i + 1}. ${url}`).join("");
        } catch (err) {
          photoNote = `${referencePhotoFiles.length} photo(s) added (upload failed)`;
          alertBox.textContent = "We couldn't upload your photos right now, but your enquiry was still sent.";
          alertBox.hidden = false;
        }
        if (submitBtn) submitBtn.disabled = false;
        if (btnLabel) btnLabel.textContent = originalLabel;
      } else {
        photoNote = `${referencePhotoFiles.length} photo(s) added`;
      }
    }

    const formattedMessage = [
      "Hello Floral Flirtss! 🌸",
      "",
      "I would love to place a custom bouquet enquiry:",
      "",
      `• Name: ${nameVal}`,
      `• Flower Type: ${flowerTypeVal}`,
      `• Preferred Colour: ${colourVal}`,
      `• Bouquet Size: ${sizeVal}`,
      `• Occasion: ${occasionVal}`,
      `• Preferred Delivery Date: ${dateVal}`,
      `• Delivery Area/Locality: ${areaVal}`,
      `• Personal Gift Message: ${giftMsgVal}`,
      `• Additional Requirements: ${reqsVal}`,
      `• Reference Photos: ${photoNote}`,
      "",
      CLOSING_CONFIRMATION_LINE
    ].join("\n");

    trackEvent("custom_bouquet_enquiry", { photos: referencePhotoFiles.length, flower_type: flowerTypeVal, occasion: occasionVal });
    const waUrl = createWhatsAppUrl(formattedMessage);
    if (waWindow) {
      waWindow.location.href = waUrl;
    } else {
      window.location.href = waUrl;
    }
  });
}

/* --------------------------------------------------------------------------
   9. PRODUCT-SPECIFIC WHATSAPP ENQUIRY BUTTONS
   -------------------------------------------------------------------------- */
function initProductEnquiries() {
  const productButtons = document.querySelectorAll(".btn-product-enquiry");

  productButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      // If it's an anchor, prevent default if we're opening WhatsApp
      const productName = button.getAttribute("data-product") || "Handmade Floral";

      const message = [
        `Hello Floral Flirtss! 🌸`,
        ``,
        `I would love to enquire about your "${productName}" collection in Hyderabad. Could you please share available shades, sizing, and customisation details?`,
        ``,
        CLOSING_CONFIRMATION_LINE
      ].join("\n");

      trackEvent("whatsapp_click", { location: "product_or_cta" });
      const waUrl = createWhatsAppUrl(message);
      window.open(waUrl, "_blank", "noopener,noreferrer");
    });
  });
}

/* --------------------------------------------------------------------------
   10. GENERAL WHATSAPP ORDER & CTA BUTTONS
   -------------------------------------------------------------------------- */
function initGeneralOrderButtons() {
  const generalButtons = document.querySelectorAll(".btn-general-order");

  generalButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const message = [
        "Hello Floral Flirtss! 🌸",
        "",
        "I'm interested in your handmade forever flowers and would love to enquire about your floral collections and custom arrangements in Hyderabad.",
        "",
        CLOSING_CONFIRMATION_LINE
      ].join("\n");

      trackEvent("whatsapp_click", { location: "product_or_cta" });
      const waUrl = createWhatsAppUrl(message);
      window.open(waUrl, "_blank", "noopener,noreferrer");
    });
  });
}

/* --------------------------------------------------------------------------
   11. BACK TO TOP BUTTON
   -------------------------------------------------------------------------- */
function initBackToTop() {
  const backToTopBtn = document.getElementById("backToTopBtn");
  if (!backToTopBtn) return;

  backToTopBtn.addEventListener("click", (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  });
}
