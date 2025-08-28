
        document.addEventListener('DOMContentLoaded', function() {
            // Password visibility toggler
            const passwordToggles = document.querySelectorAll('.password-toggle');
            
            passwordToggles.forEach(toggle => {
                toggle.addEventListener('click', function() {
                    const input = this.parentElement.querySelector('input');
                    const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
                    input.setAttribute('type', type);
                    
                    this.classList.toggle('fa-eye');
                    this.classList.toggle('fa-eye-slash');
                });
            });
            
            // Form validation
            const form = document.getElementById('signup-form');
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateForm()) {
                    // Form is valid, you can submit data to server here
                    alert('Form submitted successfully!');
                    form.reset();
                    
                    // Remove validation styles
                    document.querySelectorAll('.input-group').forEach(group => {
                        group.classList.remove('success');
                    });
                }
            });
            
            // Real-time validation
            const inputs = document.querySelectorAll('input');
            
            inputs.forEach(input => {
                // Validate on input change
                input.addEventListener('blur', function() {
                    validateField(this);
                });
                
                // Remove error when user starts typing
                input.addEventListener('input', function() {
                    const group = this.parentElement;
                    group.classList.remove('error');
                    group.classList.remove('success');
                    
                    const errorElement = group.parentElement.querySelector('.error-message');
                    errorElement.style.display = 'none';
                });
            });
            
            function validateForm() {
                let isValid = true;
                
                const fullname = document.getElementById('fullname');
                const email = document.getElementById('email');
                const password = document.getElementById('password');
                const confirmPassword = document.getElementById('confirm-password');
                const terms = document.getElementById('terms');
                
                if (!validateField(fullname)) isValid = false;
                if (!validateField(email)) isValid = false;
                if (!validateField(password)) isValid = false;
                if (!validateField(confirmPassword)) isValid = false;
                
                // Validate terms checkbox
                if (!terms.checked) {
                    isValid = false;
                    const termsLabel = terms.parentElement;
                    termsLabel.style.color = 'var(--error)';
                } else {
                    const termsLabel = terms.parentElement;
                    termsLabel.style.color = 'var(--gray)';
                }
                
                return isValid;
            }
            
            function validateField(field) {
                const value = field.value.trim();
                const group = field.parentElement;
                const errorElement = group.parentElement.querySelector('.error-message');
                
                group.classList.remove('error', 'success');
                errorElement.style.display = 'none';
                
                // Check if field is empty
                if (!value) {
                    group.classList.add('error');
                    errorElement.textContent = `${field.name} is required`;
                    errorElement.style.display = 'block';
                    return false;
                }
                
                // Email validation
                if (field.type === 'email') {
                    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailPattern.test(value)) {
                        group.classList.add('error');
                        errorElement.textContent = 'Please enter a valid email address';
                        errorElement.style.display = 'block';
                        return false;
                    }
                }
                
                // Password validation
                if (field.id === 'password') {
                    if (value.length < 8) {
                        group.classList.add('error');
                        errorElement.textContent = 'Password must be at least 8 characters';
                        errorElement.style.display = 'block';
                        return false;
                    }
                }
                
                // Confirm password validation
                if (field.id === 'confirm-password') {
                    const passwordValue = document.getElementById('password').value;
                    if (value !== passwordValue) {
                        group.classList.add('error');
                        errorElement.textContent = 'Passwords do not match';
                        errorElement.style.display = 'block';
                        return false;
                    }
                }
                
                // If all validations pass
                group.classList.add('success');
                return true;
            }
            
            // Social login buttons
            const socialButtons = document.querySelectorAll('.social-btn');
            
            socialButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const type = this.querySelector('i').classList[1];
                    let provider;
                    
                    switch (type) {
                        case 'fa-google':
                            provider = 'Google';
                            break;
                        case 'fa-facebook-f':
                            provider = 'Facebook';
                            break;
                        case 'fa-twitter':
                            provider = 'Twitter';
                            break;
                    }
                    
                    alert(`Sign up with ${provider} clicked`);
                });
            });
            
            // Mobile menu toggle
            const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
            const navLinks = document.querySelector('.nav-links');
            const navButtons = document.querySelector('.nav-buttons');
            
            mobileMenuBtn.addEventListener('click', function() {
                const isVisible = navLinks.style.display === 'flex';
                
                if (isVisible) {
                    navLinks.style.display = 'none';
                    navButtons.style.display = 'none';
                } else {
                    navLinks.style.display = 'flex';
                    navLinks.style.flexDirection = 'column';
                    navLinks.style.position = 'absolute';
                    navLinks.style.top = '100px';
                    navLinks.style.left = '0';
                    navLinks.style.width = '100%';
                    navLinks.style.background = 'white';
                    navLinks.style.padding = '20px';
                    navLinks.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
                    
                    navButtons.style.display = 'flex';
                    navButtons.style.flexDirection = 'column';
                    navButtons.style.position = 'absolute';
                    navButtons.style.top = '280px';
                    navButtons.style.left = '0';
                    navButtons.style.width = '100%';
                    navButtons.style.background = 'white';
                    navButtons.style.padding = '20px';
                    navButtons.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
                    
                    // Adjust individual elements
                    document.querySelectorAll('.nav-links li').forEach(li => {
                        li.style.margin = '10px 0';
                    });
                    
                    document.querySelector('.language-selector').style.margin = '0 0 15px 0';
                    document.querySelector('.btn-login').style.margin = '0 0 15px 0';
                    document.querySelector('.btn-signup').style.margin = '0';
                }
            });
        });
    

        // slider= document
        // why chocis us section
        document.addEventListener('DOMContentLoaded', function () {
            const slides = document.querySelectorAll('.slide');
            const dots = document.querySelectorAll('.nav-dot');
            const prevArrow = document.querySelector('.slider-arrow.prev');
            const nextArrow = document.querySelector('.slider-arrow.next');
            let currentSlide = 0;
            let slideInterval;

            // Function to show a specific slide
            function showSlide(n) {
                // Hide all slides
                slides.forEach(slide => slide.classList.remove('active'));
                dots.forEach(dot => dot.classList.remove('active'));

                // Adjust currentSlide index if out of bounds
                if (n >= slides.length) currentSlide = 0;
                else if (n < 0) currentSlide = slides.length - 1;
                else currentSlide = n;

                // Show the correct slide and activate its dot
                slides[currentSlide].classList.add('active');
                dots[currentSlide].classList.add('active');
            }

            // Function to go to next slide
            function nextSlide() {
                showSlide(currentSlide + 1);
            }

            // Start auto-sliding
            function startSlideShow() {
                slideInterval = setInterval(nextSlide, 5000);
            }

            // Stop auto-sliding
            function stopSlideShow() {
                clearInterval(slideInterval);
            }

            // Event Listeners for Dots
            dots.forEach(dot => {
                dot.addEventListener('click', function() {
                    stopSlideShow();
                    let slideIndex = parseInt(this.getAttribute('data-slide'));
                    showSlide(slideIndex);
                    startSlideShow();
                });
            });

            // Event Listeners for Arrows
            nextArrow.addEventListener('click', () => {
                stopSlideShow();
                nextSlide();
                startSlideShow();
            });
            
            prevArrow.addEventListener('click', () => {
                stopSlideShow();
                showSlide(currentSlide - 1);
                startSlideShow();
            });

            // Pause slideshow when hovering over slider
            const slider = document.querySelector('.section-slider');
            slider.addEventListener('mouseenter', stopSlideShow);
            slider.addEventListener('mouseleave', startSlideShow);

            // Start the slideshow
            startSlideShow();
        });