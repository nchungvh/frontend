$(function () {
    let dataResult = []
    $('#search').click(function () {
    	$('#result').hide();
    	$('#loading').show();
        console.log("Press a button!")
        console.log(document.getElementById('query_type').value)
        console.log(document.getElementById('src_name').value)
        console.log(document.getElementById('target_type').value)
        $.ajax({
            url: '/api/search/' + document.getElementById('query_type').value +
             '/' + document.getElementById('src_name').value + 
             '/' + document.getElementById('target_type').value +
             '/' + document.getElementById('num-of-keywords').value,
            //  '&k=10' + document.getElementById('num_return').value,
            success: function (data) {
                dataResult = data;
                // resultModels =                
                
                for (i = 0; i < data.length; i++) {
                        let idResult = '#result-model' + (i + 1)
                        // $('#result-wrapper').append('<p>' + data[i]+ '</p>');
                        

                        // $(idResult1).html('');
                        // $(idResult2).html('');
                        if(data[i]){
                            if(data[i].length  == 0){
                                $(idResult).html('');
                                $(idResult).append(
                                    `<h3 style="text-align: center;color: #999; margin: 30% 0;font-weight: 400;">No results</h3>`
                                );
    
                            }
                            else{
                                $(idResult).html('');
                                for(j=0; j<data[i].length;j++){
                                    let m = data[i][j]
                                    let value = m["value"]
                                    let address = m["address"]
                                        $(idResult).append(
                                            `
                                            <div class="w3-row">
                                            <div class="w3-col s8">
                                            <p>`+ value+ `</p>
                                            </div>
                                            <div class="w3-col s4" style=justify-content: flex-end; margin-top: 10px;">

                                            <button type="button" class="button" id=button-${i}-${j}>Detail</button>
                                            </div>
                                            </div>
                                        `
                                        );
        
                                    
                            }
        
    
                        }

                        }
                   
                           
    
                        
                        
                    }

                


                
                
                $('#result').show();
                $('#loading').hide();
            }
        });
    });
    $(document).on("click", ".button", function(e){
        let id = e.target.id;
        let i = Number(id.split("-")[1])
        let j = Number(id.split("-")[2])
        let add = dataResult[i][j]["address"]
        $("#result-detail").css("display","block")
        let idResult = "#result-detail" + " .content"
        $(idResult).html("")
        $(idResult).append(
                    `<div class="item-keyword">
                                             <div>
                                                <img src="http://icons.iconarchive.com/icons/double-j-design/childish/128/Key-icon.png"
                                                     width="18px"
                                                    height="18px"
                                                 >
                                             </div>
                                             <div style="padding: 4px;">` + add + `</div>
                                         </div>`
        )
    })
    
});

// function updateDataset() {
//     let btnChooseFiles = document.getElementsByClassName("btn-choose-file");
//     for(i=0;i<btnChooseFiles.length;i+=2){
//         datasets[i/2] = {
//             id: datasets[i/2].id,
//             metaFile: btnChooseFiles[i+1].textContent,
//             embFile: btnChooseFiles[i].textContent
//         }
//     }
// } 

function changeFile(e) {
    var fileName = e.target.files[0].name;
    $(this).parent().find('button').text(fileName);
}


function changeNumDatasets(){
    var e = document.getElementById("num-of-datasets");
    console.log(e.value);
    const numDatasets = e.value;
    document.getElementById("numDatasets").setAttribute("value",numDatasets);
    $('#listModels').html('');
    for(i=1;i<=numDatasets;i++) {
        let idModel = 'model' + i;
        $('#listModels').append(`
        <div class="upload-model">
            <h4 class="header">Model `+ i +`</h4>
            <div class="content">
                <div class="item-upload">
                    <button type="button" class="btn-choose-file" onclick="document.getElementById('meta_file_`+idModel+`').click();">Choose file</button>
                    <input type="file" name="meta_file_`+idModel+`" id="meta_file_`+idModel+`" style="display: none;" />
                </div>
            </div>
        </div>
        `);
    }
    $('input[type=file]').change(function (e) {
        var fileName = e.target.files[0].name;
        $(this).parent().find('button').text(fileName);
        // updateDataset();
    })
}