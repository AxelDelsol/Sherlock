function processText() {
    fetch('analyze_text', 
    {
        method: 'post',
        body: document.getElementById("textToAnalyze").value
    })
    .then(response => process_reponse(response))
    .then(jsonData => process_data(jsonData))
    .catch(error => process_error(error));
}

function process_reponse(response){
    clear_div();
    if (!response.ok) {
        let message = "ERROR (Code: " + response.status + ") : " + response.statusText;
        throw new Error(message);
    }
    return response.json();
}

function clear_div(){
    ["error_message", "result_people", "result_fact"]
    .forEach(element => document.getElementById(element).innerHTML = "");
}

function process_error(error) {
    let result = document.getElementById("error_message");
    result.innerHTML = error.message;
}

function process_data(jsonData){
    process_people(jsonData["people"]);
    process_facts(jsonData["facts"]);
}

function process_people(personData){
    generateDynamicTable(personData, "result_people");
}

function process_facts(factsData){
    generateDynamicTable(factsData, "result_fact");
}

function generateDynamicTable(data, container_id){
	
    if (data.length == 0) {
        var divContainer = document.getElementById(container_id);
        divContainer.innerHTML = "No data found";
    } else {
        var table = create_simple_table();
        var header_map = build_header(table, data);
        build_body(table, data, header_map);
        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        var divContainer = document.getElementById(container_id);
        divContainer.innerHTML = "";
        divContainer.appendChild(table);
    }	
}

function build_header(table, data){
    var header_map = get_headers_map(data);
        
    // CREATE TABLE HEAD .
    var tHead = document.createElement("thead");	
        
    // CREATE ROW FOR TABLE HEAD .
    var hRow = document.createElement("tr");
    
    // ADD COLUMN HEADER TO ROW OF TABLE HEAD.
    for (let key of header_map.keys()) {
            var th = document.createElement("th");
            th.innerHTML = key;
            hRow.appendChild(th);
    }
    tHead.appendChild(hRow);
    table.appendChild(tHead);

    return header_map;
}

function build_body(table, data, header_map){
    var tBody = document.createElement("tbody");	  
    for (var contact of data) {
    
            var bRow = document.createElement("tr");
            var tds = Array(header_map.size).fill(document.createElement("td"));

            Object.keys(contact)
            .sort((a,b) => header_map.get(a) - header_map.get(b))
            .forEach(function(key){
                let td = document.createElement("td");
                td.innerHTML = contact[key];
                bRow.appendChild(td);
            });
            tBody.appendChild(bRow)
    }
    table.appendChild(tBody);	
}

function create_simple_table(){
    var table = document.createElement("table");
    table.style.width = '50%';
    table.setAttribute('border', '1');
    table.setAttribute('cellspacing', '0');
    table.setAttribute('cellpadding', '5');

    return table;
}


function get_headers_map(data_array){
    var map = new Map();
    let id = 0

    for (var i = 0; i < data_array.length; i++) {
        for (var key in data_array[i]) {
            if (!map.has(key)) {
                map.set(key, id);
                ++id; 
            }
        }
    }

    return map;
}