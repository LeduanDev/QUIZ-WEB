document.addEventListener("DOMContentLoaded", function() {
    // Circular chart (doughnut)
    const ctx = document.getElementById('percentageChart').getContext('2d');
    const chartDataElement = document.getElementById('chart-data');
    const totalScore = parseInt(chartDataElement.getAttribute('data-total-score'), 10);
    const percentageCorrect = parseFloat(chartDataElement.getAttribute('data-percentage-correct'));

    const myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Correctas', 'Incorrectas'],
            datasets: [{
                label: 'Puntuación',
                data: [percentageCorrect, 100 - percentageCorrect],
                backgroundColor: [
                    'rgba(54, 162, 235, 1)',  // Color for correct answers
                    'rgba(211, 211, 211, 1)'   // Color for incorrect answers
                ],
                borderColor: 'white',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '70%',
            plugins: {
                legend: { display: false }, // Disable legend
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.label + ': ' + tooltipItem.raw + '%';
                        }
                    }
                }
            }
        }
    });

    // Linear progress bar (horizontal bar chart)
    const progressCtx = document.getElementById('linearProgressChart').getContext('2d');
    const myLinearChart = new Chart(progressCtx, {
        type: 'bar',
        data: {
            labels: [''], // Empty label to remove the extra space
            datasets: [{
                label: '', // No label
                data: [percentageCorrect],
                backgroundColor: 'rgba(54, 162, 235, 1)',  // Color for correct answers
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',  // Make it horizontal
            scales: {
                x: {
                    min: 0,
                    max: 100,  // Range from 0 to 100%
                    ticks: { stepSize: 10 }
                },
                y: {
                    display: false  // Hide y-axis labels
                }
            },
            plugins: {
                legend: { display: false }, // Disable legend
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return 'Porcentaje: ' + tooltipItem.raw + '%';
                        }
                    }
                }
            },
            responsive: true,
            maintainAspectRatio: false  // Prevent chart from being stretched
        }
    });
});
