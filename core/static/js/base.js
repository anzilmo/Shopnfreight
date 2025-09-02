// Simple JavaScript to demonstrate mobile menu toggle
        document.querySelector('.menu-toggle').addEventListener('click', function() {
            alert('Menu toggle clicked! In a real implementation, this would open a mobile menu.');
        });
        
        // Language selector functionality
        document.querySelectorAll('.language-dropdown li').forEach(item => {
            item.addEventListener('click', function() {
                const lang = this.getAttribute('data-lang');
                document.querySelector('.selected-language').textContent = this.textContent;
                alert(`Language changed to ${this.textContent} (${lang})`);
            });
        });