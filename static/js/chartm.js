$('Document').ready(function(){
				chart= new CanvasJS.Chart("grafica1",{
					title:{
						text:"Clima en Bogotá",
						fontColor:"#7986cb"
					},
					data:[
					{
						type:"spline",
						dataPoints: []
					}]
				});

				chart2= new CanvasJS.Chart("grafica2",{
					title:{
						text:"Números aleatorios",
						fontColor:"#7986cb"
					},
					data:[{
						type:"spline",
						dataPoints:[]
					}]
				});

				chart3= new CanvasJS.Chart("grafica3",{
					title:{
						text:"Clima en Manizales",
						fontColor:"#7986cb"
					},
					data:[
					{
						type:"spline",
						dataPoints:[]
					}]
				});

				chart4= new CanvasJS.Chart("grafica4",{
					title:{
						text:"Clima en Chigorodó",
						fontColor:"#7986cb"
					},
					data:[
					{
						type:"spline",
						dataPoints:[]
					}]
				});
			});