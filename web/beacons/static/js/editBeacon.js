(function editBeacon(){
    $(document).ready(function(){
        editBeacon.init();
    });

    editBeacon.init = function(){
    	editBeacon.description = $("#description")[0];
        $("#description")[0].value = $("#description")[0].value.replace(/%20/g, " ");

    	$("form")[0].onsubmit = editBeacon.validateAndSubmit;
    }

    editBeacon.validateAndSubmit = function(e){
    	if(editBeacon.description.value.length == 0){
    		e.preventDefault();
    	}
    }
})();