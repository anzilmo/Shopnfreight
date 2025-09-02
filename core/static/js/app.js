//step 1: get DOM
let nextDom = document.getElementById('next');
let prevDom = document.getElementById('prev');

let carouselDom = document.querySelector('.carousel');
let SliderDom = carouselDom.querySelector('.carousel .list');
let thumbnailBorderDom = document.querySelector('.carousel .thumbnail');
let thumbnailItemsDom = thumbnailBorderDom.querySelectorAll('.item');
let timeDom = document.querySelector('.carousel .time');

thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
let timeRunning = 3000;
let timeAutoNext = 7000;

nextDom.onclick = function(){
    showSlider('next');    
}

prevDom.onclick = function(){
    showSlider('prev');    
}
let runTimeOut;
let runNextAuto = setTimeout(() => {
    next.click();
}, timeAutoNext)
function showSlider(type){
    let  SliderItemsDom = SliderDom.querySelectorAll('.carousel .list .item');
    let thumbnailItemsDom = document.querySelectorAll('.carousel .thumbnail .item');
    
    if(type === 'next'){
        SliderDom.appendChild(SliderItemsDom[0]);
        thumbnailBorderDom.appendChild(thumbnailItemsDom[0]);
        carouselDom.classList.add('next');
    }else{
        SliderDom.prepend(SliderItemsDom[SliderItemsDom.length - 1]);
        thumbnailBorderDom.prepend(thumbnailItemsDom[thumbnailItemsDom.length - 1]);
        carouselDom.classList.add('prev');
    }
    clearTimeout(runTimeOut);
    runTimeOut = setTimeout(() => {
        carouselDom.classList.remove('next');
        carouselDom.classList.remove('prev');
    }, timeRunning);

    clearTimeout(runNextAuto);
    runNextAuto = setTimeout(() => {
        next.click();
    }, timeAutoNext)
}

// Creat accounts seiontion 
document.addEventListener('DOMContentLoaded', function() {
            const steps = document.querySelectorAll('.info-step');
            
            // Function to check if an element is in the viewport
            function isInViewport(element) {
                const rect = element.getBoundingClientRect();
                return (
                    rect.top >= 0 &&
                    rect.left >= 0 &&
                    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                );
            }
            
            // Function to handle scroll events
            function handleScroll() {
                steps.forEach(step => {
                    if (isInViewport(step)) {
                        step.classList.add('visible');
                    }
                });
            }
            
            // Initial check on page load
            handleScroll();
            
            // Listen for scroll events
            window.addEventListener('scroll', handleScroll);
            
            // Add some extra animation for the connectors
            const connectors = document.querySelectorAll('.info-connector');
            
            function animateConnectors() {
                connectors.forEach((connector, index) => {
                    setTimeout(() => {
                        connector.style.opacity = '1';
                        connector.style.transition = 'opacity 0.8s ease';
                    }, 1000 + index * 300);
                });
            }
            
            // Animate connectors when steps become visible
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        animateConnectors();
                    }
                });
            }, { threshold: 0.5 });
            
            observer.observe(document.querySelector('.info-steps'));
        });


// why choice

document.addEventListener('DOMContentLoaded', function() {
            // Animate elements on page load
            setTimeout(function() {
                document.querySelector('.h-why').classList.add('visible');
                document.querySelector('.subtitle').classList.add('visible');
                document.querySelector('.description-why').classList.add('visible');
                document.querySelectorAll('.option').forEach(option => {
                    option.classList.add('visible');
                });
                document.querySelector('.image-content').classList.add('visible');
            }, 300);
            
            // Option click interaction
            document.querySelectorAll('.option').forEach(option => {
                option.addEventListener('click', function() {
                    this.classList.toggle('active');
                    const paragraph = this.querySelector('.p-why');
                    paragraph.style.color = this.classList.contains('active') ? '#3498db' : '#666';
                });
            });
            
            // Learn More button functionality
            document.getElementById('learnMoreBtn').addEventListener('click', function() {
                const statsContainer = document.getElementById('statsContainer');
                statsContainer.classList.add('visible');
                
                // Animate counting stats
                animateCounter('stat1', 0, 120, 2000);
                animateCounter('stat2', 0, 10000, 2000);
                animateCounter('stat3', 0, 50000, 2000);
            });
            
            // Counter animation function
            function animateCounter(elementId, start, end, duration) {
                let obj = document.getElementById(elementId);
                let current = start;
                let range = end - start;
                let increment = end > start ? 1 : -1;
                let stepTime = Math.abs(Math.floor(duration / range));
                let timer = setInterval(function() {
                    current += increment;
                    obj.textContent = current.toLocaleString();
                    if (current == end) {
                        clearInterval(timer);
                    }
                }, stepTime);
            }
            
            // Image hover effect with JS fallback
            const image = document.querySelector('.image-content img');
            image.addEventListener('mouseover', function() {
                this.style.transform = 'scale(1.03)';
            });
            
            image.addEventListener('mouseout', function() {
                this.style.transform = 'scale(1)';
            });
        });

