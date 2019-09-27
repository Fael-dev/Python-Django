$(document).ready(function(){

     var baseUrl = 'http://localhost:8000/';
     var filter = $('#filter');
	 var deleteBtn = $('.delete-btn');
	 var searchBtn = $('#search-btn');
	 var searchForm = $('#search-form'); 

	 $(deleteBtn).on('click', function(e){

	 		e.preventDefault();

	 		var delLink =$(this).attr('href');
	 		var result = confirm('Quer deletar o item selecionado?');

	 		if(result) {
	 			window.location.href = delLink;
	 		}
	 });

	 $(searchBtn).on('click', function() {
	 	searchForm.submit();
	 });

	 $(filter).change(function(){
	 	var filter = $(this).val();
	 	window.location.href = baseUrl + '?filter=' +filter;
	 });

});