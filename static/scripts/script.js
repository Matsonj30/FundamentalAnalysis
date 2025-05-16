function changeTabs(tabSelected){
  allStatements = document.getElementsByClassName("statement")

  for(i = 0; i< allStatements.length; i+= 1){
    allStatements[i].style.display = "none"
  }
  switch(tabSelected){
    case "incomeStatement":
      allStatements[0].style.display = "block"
      break;
    case "balanceSheet":
      allStatements[1].style.display = "block"
      break;
    case "cashFlow":
      allStatements[2].style.display = "block"
      break;
    default:
      allStatements[0].style.display = "block"
    break;
  }
}

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
        createChartContainer(datesList.reverse(), dataList.reverse(), rowName)
    }
    
}

function createChartContainer(datesList, values, rowName) {
  const win = window.open("", "_blank", "width=700,height=500")

  // Chart.js CDN and basic HTML content
  win.document.write(`
    <!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>${rowName} Chart</title>
          <link rel="stylesheet" href="/static/style.css">
          <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
      </head>
      <body>
        <h2>${rowName}</h2>
        <canvas id="chartCanvas" width="600" height="400"></canvas>
        <script>
          const ctx = document.getElementById("chartCanvas").getContext("2d");
          new Chart(ctx, {
            type: 'line',
            data: {
              labels: ${JSON.stringify(datesList)},
              datasets: [{
                label: "${rowName}",
                data: ${JSON.stringify(values)},
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
                  text: "${rowName} Over Time"
                },
                 legend:{
                  labels:{
                    color:"white"
                  }
                }
              }
               
            }
          });
        </script>
      </body>
    </html>
  `);

  win.document.close();
}