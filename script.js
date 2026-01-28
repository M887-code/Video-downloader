// कोई अतिरिक्त JS नहीं चाहिए, लेकिन अगर जरूरत हो तो यहां जोड़ें
document.addEventListener('DOMContentLoaded', function() {
    // फॉर्म वैलिडेशन
    const form = document.querySelector('form');
    form.addEventListener('submit', function(e) {
        const url = document.querySelector('input[name="url"]').value;
        if (!url.includes('youtube.com') && !url.includes('youtu.be')) {
            alert('केवल YouTube URLs समर्थित हैं।');
            e.preventDefault();
        }
    });
});