var temperature = document.getElementById('temperature');
var apikey = document.getElementById('apikey').value ;


function getdevice(){
    var requests = $.get('http://127.0.0.1:8000/'+'api/'+'node/'+apikey+'/');
    var tm = requests.done(function (result){
        var today = new Date();
        var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
        console.log(result);
        addData(temp_chart, time, result.temperature);
        addData(humid_chart, time, result.humidity);
        addData(moist_chart, time, result.moisture);
        addData(light_chart, time, result.light);
        document.getElementById("card-temp").innerHTML = result.temperature;
        document.getElementById("card-moisture").innerHTML = result.humidity;
        document.getElementById("card-humidity").innerHTML = result.moisture;
        document.getElementById("card-light").innerHTML = result.light;
        if (couter >= 10 ){
            removeData(temp_chart);
            removeData(humid_chart);
            removeData(moist_chart);
            removeData(light_chart);
        }
        couter++;

        setTimeout(getdevice, 2000);
        
    
    });
    
}

//temperature chart object created 
var temp_chart = new Chart(temperature, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(244, 67, 54, 0.1)',
            borderColor:'rgba(244, 67, 54, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var humidity = document.getElementById('humidity');
var humid_chart = new Chart(humidity, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Humidity W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(33, 150, 243, 0.1)',
            borderColor:'rgba(33, 150, 243, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

var moisture = document.getElementById('moisture');
var moist_chart = new Chart(moisture, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Moisture W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(0, 150, 136, 0.1)',
            borderColor:'rgba(0, 150, 136, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


var light = document.getElementById('light');
var light_chart = new Chart(light, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Light W.R.T. Time',
            data: [],
            fill:true,
            backgroundColor: 'rgba(255, 152, 0, 0.1)',
            borderColor:'rgba(255, 152, 0, 1)',
            borderWidth: 3
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.shift();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
    chart.update();
}

var couter = 0; 

getdevice();
