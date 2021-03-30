$(function() {
    let dataResult = []
    $('#search').click(function() {
        $('#result').hide();
        $('#loading').show();
        console.log("Press a button!")
        console.log(document.getElementById('src_name').value)
        $.ajax({
            url: '/api/search/' + document.getElementById('src_name').value +
                '/' + document.getElementById('num-of-keywords').value + '/' + document.getElementById('category').value,
            success: function(data) {
                dataResult = data;
                for (i = 0; i < data.length; i++) {
                    let idResult = '#knn-' + i; //#result-model' + (i + 1)
                    if (data[i]) {
                        if (data[i].length == 0) {
                            $(idResult).html('');
                            $(idResult).append(
                                `<h3 style="margin: 0 20%; text-align: center;color: #999;font-weight: 400;">No results</h3>`
                            );

                        } else {
                            $(idResult).html('');
                            for (j = 0; j < data[i].length; j++) {
                                let m = data[i][j]
                                let value = m["value"]
                                let address = m["address"]
                                let com_cate = m["cate"]
                                console.log(m);
                                $(idResult).append(
                                    `
                                    <div class="dropdown">
                                    <span class="dropbtn">` + value + `</span>
                                    <div class="dropdown-content" id=button-${i}-${j}>
                                    </div>
                                    </div>
                                `
                                );
                                let iddrop = "#button-" + i + "-" + j;
                                for (var index = 0; index < com_cate.length; index++) {
                                    $(iddrop).append(
                                        `<a>` + com_cate[index] + `</a>`
                                    )
                                }
                            }


                        }

                    }
                }

                $('#result').show();
                $('#loading').hide();
            }
        });
    });

    //// <p>` + value + `:<a href="` + address + `">Go to company page</a> </p>

    $(document).on("click", ".button", function(e) {
        let id = e.target.id;
        let i = Number(id.split("-")[1])
        let j = Number(id.split("-")[2])
        let add = dataResult[i][j]["cate"]
            // $("#result-detail").css("display", "block")
        let idResult = "#button-" + i + "-" + j;
        $(idResult).html("")
            // $(idResult).append(
            //     `<div class="item-keyword">
            //     <hr  size="100px" background-color="black"/>
            //     <hr  size="100px" background-color="black"/>
            //             <div>
            //             <img src="http://icons.iconarchive.com/icons/double-j-design/childish/128/Key-icon.png"
            //                     width="18px"
            //                 height="18px"
            //                 >
            //             </div>
            //             <div style="padding: 4px;">` + add[0] + `</div>
            //         </div>`
            // )
        for (var index = 1; index < add.length; index++) {
            $(idResult).append(
                `<a href="#">` + add[index] + `</a>`
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

function changeCate() {
    let dataResult = []
        // $('#src_name').click(function() {
    console.log(document.getElementById('src_name').value)
    $.ajax({
            url: '/api/cate/' + document.getElementById('src_name').value,
            success: function(data) {
                dataResult = data;
                let idResult = '#category'; //#result-model' + (i + 1)
                $(idResult).html('');
                $(idResult).append(`<option value="Default">Default</option>`);
                for (i = 0; i < data.length; i++) {
                    $(idResult).append(`<option value="` + data[i] + `">` + data[i] + `</option>`);
                }
            }
        })
        // })
}