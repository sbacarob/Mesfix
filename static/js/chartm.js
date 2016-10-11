//En este archivo se incluyen métodos para manejar las gráficas. 
//Incluyenddo métodos para establecer elementos de las gráficas y para actualizarlas

/**
**** Esta función se usa para inicializar las gráficas de canvasjs cuando el documento ya está listo
**/
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


/**
**** Función que actualiza periodicamente la información. Esta función es llamada cada minuto y hace una petición GET 
**** a cada url para actualizar la interfaz.
**/
function updateData(){
	var dt= new Date()
	$.get('http://104.131.16.36',function(data, statusText, xhr){
		if(xhr.status==200){
			cl1=parseFloat(data);	
			$('#serv-status-1').html('On')
			$('#serv-status-1').css('color','green')		
		}
		else{
			cl1=null;
			$('#serv-status-1').html('Down <span class="fa fa-wrench" style="cursor:pointer" id="fix-1"></span>')
			$('#serv-status-1').css('color','#e53935')		
		}
		chart.options.data[0].dataPoints.push({x:dt,y:cl1});
		chart.render();
	});
	$.get('http://104.131.59.50',function(data, statusText, xhr){
		if(xhr.status==200){
			rdm=parseInt(data);			
			$('#serv-status-2').html('On')
			$('#serv-status-2').css('color','green')		
		}
		else{
			rdm=null;
			$('#serv-status-2').html('Down <span class="fa fa-wrench" style="cursor:pointer" id="fix-2"></span>')
			$('#serv-status-2').css('color','#e53935')		
		}
		chart2.options.data[0].dataPoints.push({x:dt,y:rdm});
		chart2.render();
	});
	$.get('http://104.131.90.195',function(data, statusText, xhr){
		if(xhr.status==200){
			cl2=parseFloat(data);			
			$('#serv-status-3').html('On')
			$('#serv-status-3').css('color','green')		
		}
		else{
			cl2=null;
			$('#serv-status-3').html('Down <span class="fa fa-wrench" style="cursor:pointer" id="fix-3"></span>')
			$('#serv-status-3').css('color','#e53935')		
		}
		chart3.options.data[0].dataPoints.push({x:dt,y:cl2});
		chart3.render();
	});
	$.get('http://104.131.93.15',function(data, statusText, xhr){
		if(xhr.status==200){
			cl3=parseFloat(data);		
			$('#serv-status-4').html('On')
			$('#serv-status-4').css('color','green')		
		}
		else{
			cl3=null;
			$('#serv-status-4').html('Down <span class="fa fa-wrench" style="cursor:pointer" id="fix-1"></span>')
			$('#serv-status-4').css('color','#e53935')		
		}
		chart4.options.data[0].dataPoints.push({x:dt,y:cl3});
		chart4.render();
	});
}