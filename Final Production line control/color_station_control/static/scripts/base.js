$(document).ready(function () {
  
  
  $("select").chosen({
    no_results_text: "Oops, nothing found!",
    disable_search_threshold: 10
  });
  
  $('#id_piece_chosen').css('width', '10rem');
  $('.chosen-search-input').css('width', '8rem');
  // $("#id_station").chosen({
  //   no_results_text: "Oops, nothing found!"
  // });
  




  $("#id_date").pDatepicker({
    initialValueType: 'persian',
    format: 'YYYY-MM-DD',
    calendar:{
      persian:{
        locale:'en'
      }
    }
    
  });


});





x=$.getJSON("/stationjson/",
  function (data, textStatus, jqXHR) {
    let stations=Object.keys(data)
    let datapoints=[]
  
    for(station of stations)
      datapoints.push({label: station ,y:data[station]['reports']})
    
    console.log(datapoints)

    var chart = new CanvasJS.Chart("chartContainer", {
      animationEnabled: true,
      theme: "light2", // "light1", "light2", "dark1", "dark2"
      title: {
        text: "تمامی ایستگاه ها"
      },
      
      axisY: {
        
      },
      data: [{
        type: "column",
        // yValueFormatString: "$#,##0.00",
        dataPoints:datapoints
      }]
    });
    
    chart.render();


    
  }
)

