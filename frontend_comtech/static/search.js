$(function() {
    let dataResult = []
    $('#search').click(function() {
        $('#result').hide();
        $('#loading').show();
        console.log("Press a button!")
        console.log(document.getElementById('src_name').value)
        $.ajax({
            url: '/api/search/' + document.getElementById('src_name').value +
                '/' + document.getElementById('num-of-keywords').value,
            success: function(data) {
                dataResult = data;
                for (i = 0; i < data.length; i++) {
                    let idResult = '#knn-' + i; //#result-model' + (i + 1)
                    if (data[i]) {
                        console.log(data[i]);
                        if (data[i].length == 0) {
                            $(idResult).html('');
                            $(idResult).append(
                                `<h3 style="margin: 0 20%; text-align: center;color: #999;font-weight: 400;">No results</h3>`
                            );

                        } else {
                            $(idResult).html('');
                            let temp = ``;
                            for (j = 0; j < data[i].length; j++) {
                                let m = data[i][j]
                                let value = m["value"]
                                console.log(value);
                                temp +=
                                    `
                                    <div class="w3-row" style="margin:0 10%">
                                    <div class="w3-col s8">
                                    <p>` + value + `</p>
                                    </div>
                                    <div class="w3-col s4" style=justify-content: flex-end; margin-top: 10px;">

                                    </div>
                                    

                                    </div>
                                `
                            }

                            $(idResult).html(temp);


                        }

                    }
                }
                $('#result').show();
                $('#loading').hide();
            }
        });
    });

    // Up search:
    $('#upsearch').click(function() {
        $('#result').hide();
        $('#loading').show();
        console.log("Press a button!")
        console.log(document.getElementById('src_name').value)
        $.ajax({
            url: '/api/upsearch/' + document.getElementById('src_name').value +
                '/' + document.getElementById('num-of-keywords').value,
            success: function(data) {
                dataResult = data;
                for (i = 0; i < data.length; i++) {
                    let idResult = '#knn-' + i; //#result-model' + (i + 1)
                    if (data[i]) {
                        console.log(data[i]);
                        if (data[i].length == 0) {
                            $(idResult).html('');
                            $(idResult).append(
                                `<h3 style="margin: 0 20%; text-align: center;color: #999;font-weight: 400;">No results</h3>`
                            );

                        } else {
                            $(idResult).html('');
                            let temp = ``;
                            for (j = 0; j < data[i].length; j++) {
                                let m = data[i][j]
                                let value = m["value"]
                                console.log(value);
                                temp +=
                                    `
                                    <div class="w3-row" style="margin:0 10%">
                                    <div class="w3-col s8">
                                    <p>` + value + `</p>
                                    </div>
                                    <div class="w3-col s4" style=justify-content: flex-end; margin-top: 10px;">

                                    </div>
                                    

                                    </div>
                                `
                            }

                            $(idResult).html(temp);


                        }

                    }
                }
                $('#result').show();
                $('#loading').hide();
            }
        });
    });


    // down search
    $('#downsearch').click(function() {
        $('#result').hide();
        $('#loading').show();
        console.log("Press a button!")
        console.log(document.getElementById('src_name').value)
        $.ajax({
            url: '/api/downsearch/' + document.getElementById('src_name').value +
                '/' + document.getElementById('num-of-keywords').value,
            success: function(data) {
                dataResult = data;
                for (i = 0; i < data.length; i++) {
                    let idResult = '#knn-' + i; //#result-model' + (i + 1)
                    if (data[i]) {
                        console.log(data[i]);
                        if (data[i].length == 0) {
                            $(idResult).html('');
                            $(idResult).append(
                                `<h3 style="margin: 0 20%; text-align: center;color: #999;font-weight: 400;">No results</h3>`
                            );

                        } else {
                            $(idResult).html('');
                            let temp = ``;
                            for (j = 0; j < data[i].length; j++) {
                                let m = data[i][j]
                                let value = m["value"]
                                console.log(value);
                                temp +=
                                    `
                                    <div class="w3-row" style="margin:0 10%">
                                    <p>` + value + `</p>
                                    </div>
                                `
                            }

                            $(idResult).html(temp);


                        }

                    }
                }
                $('#result').show();
                $('#loading').hide();
            }
        });
    });


    $(document).on("click", ".button", function(e) {
        let id = e.target.id;
        let i = Number(id.split("-")[1])
        let j = Number(id.split("-")[2])
        let add = dataResult[i][j]["cate"]
        $("#result-detail").css("display", "block")
        let idResult = "#result-detail"
        $(idResult).html("")
        $(idResult).append(
            `<div class="item-keyword">
            <hr  size="100px" background-color="black"/>
            <hr  size="100px" background-color="black"/>
                    <div>
                    <img src="http://icons.iconarchive.com/icons/double-j-design/childish/128/Key-icon.png"
                            width="18px"
                        height="18px"
                        >
                    </div>
                    <div style="padding: 4px;">` + add[0] + `</div>
                </div>`
        )
        for (var index = 1; index < add.length; index++) {
            $(idResult).append(
                `<div class="item-keyword">
                    <div>
                    <img src="http://icons.iconarchive.com/icons/double-j-design/childish/128/Key-icon.png"
                            width="18px"
                        height="18px"
                        >
                    </div>
                    <div style="padding: 4px;">` + add[index] + `</div>
                </div>`
            )
        }

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


function changeNumDatasets() {
    var e = document.getElementById("num-of-datasets");
    console.log(e.value);
    const numDatasets = e.value;
    document.getElementById("numDatasets").setAttribute("value", numDatasets);
    console.log(document.getElementById("numDatasets"));
    $('#listModels').html('');
    for (i = 1; i <= numDatasets; i++) {
        let idModel = 'model ' + i;
        $('#listModels').append(`<div class="upload-model">
        <h4 class="header">model ` + i + `</h4>
        <div class="content">
            <div class="item-upload">
                <button type="button" class="btn-choose-file" onclick="document.getElementById('knn` + i + `').click();">Model ` + i + `</button>
                <input type="file" name="knn` + i + `" id="knn` + i + `" style="display: none;" />
            </div>
        </div>
    </div>`);
    }
    $('input[type=file]').change(function(e) {
        var fileName = e.target.files[0].name;
        $(this).parent().find('button').text(fileName);
        // updateDataset();
    })
}