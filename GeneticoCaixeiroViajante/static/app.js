var app = angular.module("app", ['ngResource']);

app.controller("CalculusController",["$scope","KnowledgeResource",function($scope, KnowledgeResource){
	$scope.request = 
	{ 
		populationSize : 0,
		mutationRate : 0,
		iterationsQuantity : 0,
		graphData :{
			vectors : [],
			edges : []
		},
		selectionStrategy : ''
	};

	$scope.backendRequest = {};
	$scope.result = {};

	$scope.pendingRequests = 0;	
	$scope.step = 'form';

	var added = 0;
	$scope.addVector = function(){
		added++;
		var name = $scope.newVector || added.toString();
		$scope.request.graphData.vectors.push(name);
		$scope.newVector = '';
		renewEdges();
		//draw();
	};

	$scope.removeVector = function(index){
		$scope.request.graphData.vectors.splice(index,1);
		renewEdges();
		//draw();
	};

	$scope.calculate = function () {
		$scope.backendRequest = angular.copy($scope.request); 
 		addReverseEdges();
 		parseWeightValues();
		$scope.pendingRequests++;
		KnowledgeResource.calculate(
			$scope.backendRequest,
			function  (response) {
				$scope.result = response;
				$scope.pendingRequests--;
				$scope.step = 'result';
			},
			function(error){
				alert(error);
				$scope.pendingRequests--;
			});
	};

	var parseWeightValues = function(){
		$scope.backendRequest.graphData.edges.forEach(function(i){
			i.weight = parseInt(i.weight);
		});
	};

	var addReverseEdges = function(){
		var reverseEdges = [];

		$scope.request.graphData.edges.forEach(function(i){
			edgeObj = {vectorOne: i.vectorTwo, vectorTwo : i.vectorOne, weight : i.weight};
			reverseEdges.push(edgeObj);
		});

		$scope.backendRequest.graphData.edges = $scope.backendRequest.graphData.edges.concat(reverseEdges);
	};

	var renewEdges = function(){
		var addedItems = []
		$scope.request.graphData.edges = [];
		var vectors = $scope.request.graphData.vectors;

		vectors.forEach(function(vector){
			addedItems.push(vector);
			var remainingVectors = vectors.where(function(i){ 
				return addedItems.all(function(it){ return it != i; }) 
			});

			remainingVectors.forEach(function(remaining){ 
				edgeObj = {vectorOne: vector, vectorTwo : remaining, weight : 1};
				$scope.request.graphData.edges.push(edgeObj);
			});

		});
	};

	var draw = function(){	
		var sigInst = new sigma('container');
		sigInst.graph.addNode('hello', {
						   id: 'n0',
					       label: 'Hello',
					       x: 0,
					       y: 3,
					       size: 1,
					       color: '#f00'
						});		
	};

	$scope.$watch('request.populationSize',function(val,old){
       $scope.request.populationSize = parseInt(val); 
    });
	$scope.$watch('request.mutationRate',function(val,old){
       $scope.request.mutationRate = parseInt(val); 
    });
	$scope.$watch('request.iterationsQuantity',function(val,old){
       $scope.request.iterationsQuantity = parseInt(val); 
    });

}]);