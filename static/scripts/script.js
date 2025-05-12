function graphRow(rowName){
    dataColumns = document.getElementById(rowName).querySelectorAll("td")
    dates = document.getElementById("row-date").querySelectorAll("td")

    const datesSliced = Array.from(dates).slice(1,-1)
    const datesList = []
    const dataList = []

    Array.from(datesSliced).forEach(element => {
       datesList.push(element.innerHTML)
    });
    Array.from(dataColumns).forEach(element => {
        const number = Number(element.innerHTML)
        if (!isNaN(number)){
            dataList.push(element.innerHTML)
        }
        
    });
    if (dataList.length > 0){
        //Reverse so the chart reads left to right 
        createChartContainer(datesList.reverse(), dataList.reverse())
    }
    
}

function createChartContainer(datesList, values) {
  // Step 1: Destroy the previous chart instance if it exists
  if (window.myChart) {
    window.myChart.destroy();
    window.myChart = null;
  }

  // Step 2: Remove the old canvas (if any)
  const existing = document.getElementById("myChart");
  if (existing) existing.remove();

  // Step 3: Create and add a new canvas
  const canvas = document.createElement("canvas");
  canvas.id = "myChart";
  canvas.width = 600;
  canvas.height = 400;
  document.body.appendChild(canvas);

   // Step 4: Render the new chart
  const ctx = canvas.getContext("2d");
  window.myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: datesList,
      datasets: [{
        label: 'Metric',
        data: values,
        borderColor: 'green',
        borderWidth: 2,
        fill: false,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: dataColumns[0].innerHTML
        }
      }
    }
  });
}
