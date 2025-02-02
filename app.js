// Interactive Skills Radar Chart
const ctx = document.getElementById('skills-radar').getContext('2d');
new Chart(ctx, {
    type: 'radar',
    data: {
        labels: ['Python', 'SQL', 'Data Engineering', 'Visualization', 'AWS'],
        datasets: [{
            label: 'Proficiency',
            data: [90, 85, 80, 95, 75],
            backgroundColor: 'rgba(0, 123, 255, 0.2)',
            borderColor: 'rgba(0, 123, 255, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scale: {
            angleLines: { display: false },
            ticks: { display: false }
        }
    }
});

// Contact Form Validation
const form = document.getElementById('contact-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    // Add your preferred email service logic here (e.g., EmailJS)
    alert('Message Sent! I\'ll get back to you soon.');
    form.reset();
});
