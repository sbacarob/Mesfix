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

function updateData(){
	var dt= new Date()
	$.get('http://mt-ds1.herokuapp.com',function(data){
		cl1=parseFloat(data);
		chart.options.data[0].dataPoints.push({x:dt,y:cl1});
		chart.render();
	});
	$.get('http://mt-ds2.herokuapp.com',function(data){
		rdm=parseInt(data);
		chart2.options.data[0].dataPoints.push({x:dt,y:rdm});
		chart2.render();
	});
	$.get('http://mt-ds3.herokuapp.com',function(data){
		cl2=parseFloat(data);
		chart3.options.data[0].dataPoints.push({x:dt,y:cl2});
		chart3.render();
	});
	$.get('http://mt-ds4.herokuapp.com',function(data){
		cl3=parseFloat(data);
		chart4.options.data[0].dataPoints.push({x:dt,y:cl3});
		chart4.render();
	});
}