
    function toggleMobileDropdown() {
      document.getElementById('mobileDropdown').classList.toggle('show');
    }

    window.addEventListener('resize', function () {
      const dropdown = document.getElementById('mobileDropdown');
      if (window.innerWidth > 768 && dropdown.classList.contains('show')) {
        dropdown.classList.remove('show');
      }
    });
    const barCtx = document.getElementById('barChart').getContext('2d');
    new Chart(barCtx, {
      type: 'bar',
      data: {
        labels: ['Corn', 'Rice', 'Tomato', 'Onion', 'Lettuce'],
        datasets: [{
          label: 'Compatible Samples',
          data: [12, 9, 7, 5, 3],
          backgroundColor: '#f1b700'
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: true }
        }
      }
    });

    const lineCtx = document.getElementById('lineChart').getContext('2d');
    new Chart(lineCtx, {
      type: 'line',
      data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [{
          label: 'Sessions',
          data: [5, 12, 20, 18, 25, 30],
          borderColor: '#f1b700',
          backgroundColor: 'rgba(241, 183, 0, 0.2)',
          fill: true,
          tension: 0.4
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: { beginAtZero: true }
        }
      }
    });
