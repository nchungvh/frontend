$(function () {
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
                console.log(data);
                // resultModels =                
                
                for (i = 0; i < data.length; i++) {
                        let idResult1 = '#result1-model' + (i + 1);
                        let idResult2 = '#result2-model' + (i + 1);
                        let idResult = '#result-model' + (i + 1) + " .content"
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
                                $(idResult1).html('');
                                $(idResult2).html('');
                                


        
                                for(j=0; j<data[i].length;j++){
                                    console.log(data[i][j])
                                    let m = data[i][j]
                                    let value = m["value"]
                                    let address = m["address"]
                                        $(idResult1).append(
                                            `
                                            <div class="item-keyword">
                                            <div>
                                                <img src="http://icons.iconarchive.com/icons/double-j-design/childish/128/Key-icon.png"
                                                    width="18px"
                                                    height="18px"
                                                >
                                            </div>
                                            <div style="padding: 4px;">` + value + `</div>
                                        </div>
                                        `
                                        );
                                        $(idResult2).append(
                                            `
                                            <div class="item-keyword">
                                            <div>
                                                <img src="http://icons.iconarchive.com/icons/double-j-design/childish/128/Key-icon.png"
                                                    width="18px"
                                                    height="18px"
                                                >
                                            </div>
                                            <div style="padding: 4px;">` + address + `</div>
                                        </div>
                                        `
                                        )


        
                                    
                            }
        
    
                        }

                        }
                   
                           
    
                        
                        
                    }

                


                
                
                $('#result').show();
                $('#loading').hide();
            }
        });
    });
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