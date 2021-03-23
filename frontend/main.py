from flask import *
from model import QueryMachine
from utils import *
from collections import defaultdict
import json
import sys
# import pymongo

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
query_machine = []  # QueryMachine()
queryMachines = []
# NUM_MODEL = 0
# WIDTH = 90/NUM_MODEL
@app.route('/')
def upload():
    WIDTH = 1
    # return render_template("file_upload_form.html")
    NUM_MODEL = 0
    dataFiles = []
    for i in range(NUM_MODEL):
        dataFiles.append({
            'width': WIDTH,
            "id": "knn" + str(i+1),
            "metaFile": "Choose file",
            "embFile": "Choose file"
        })
    tree = {
        "id": "taxonomy",
        "metaFile": "Choose file",
        "embFile": "Choose file"
    }
    return render_template("demo.html", dataFiles = dataFiles, taxonomy =tree, name_dict=[])


def clean(string):
    return string.replace('"', '\\"')


@app.route('/success', methods=['POST'])
def success():
    dataFiles = []
    if request.method == 'POST':
        global NUM_MODEL
        NUM_MODEL = int(request.form['numDatasets'])
        # numDatasets = int(request.form['numDatasets'])
        global WIDTH
        WIDTH = 90/NUM_MODEL
        global queryMachines
        queryMachines = []
        # Dictionary from type (comp, tech) to list of comps, techs
        name_dict = {}
        knns = []
        for i in range(NUM_MODEL):
            meta_f = request.files['knn' + str(i+1)]
            assert meta_f.filename.endswith('json')
            meta_f.save("temp_" + meta_f.filename)
            knns.append(get_knn("temp_" + meta_f.filename))
            dataFiles.append({
                'width': WIDTH,
                "id": "knn" + str(i+1),
                "metaFile":  meta_f.filename[:-5]
            })
        
        meta_f = request.files['taxonomy']
        meta_f.save("temp_" + meta_f.filename)
        taxonomy = get_taxonomy("temp_" + meta_f.filename)
        tree = {
            "id": "taxonomy",
            "metaFile":  meta_f.filename[:-5]
        }


        query_machine = QueryMachine()
        query_machine.update_data(knns, taxonomy)
        queryMachines.append(query_machine)
        print("qmmmmmm", len(queryMachines))
        name_dict = sorted(list(knns[0].keys()))

        return render_template("demo.html", dataFiles=dataFiles, taxonomy = tree, name_dict=name_dict)


@app.route("/api/search/<src_name>/<k>", methods=["GET"])
def search(src_name, k):
    # colect = mongo_db['kstn']
    # import pdb
    # pdb.set_trace()
    results = []
    print("queryMachines", len(queryMachines))
    global NUM_MODEL
    for qMachine in queryMachines:
        for i in range(NUM_MODEL):
            names = qMachine.search(src_name, i, int(k))
            adds = []
            for i, name in enumerate(names):
                info = {}

                info["value"] = name
                adds.append(info)
            print(adds)
            results.append(adds)

        # results.append(qMachine.search(src_type, src_name, target_type,int(k)))

    return jsonify(results), 200

@app.route("/api/upsearch/<src_name>/<k>", methods=["GET"])
def upsearch(src_name, k):
    global queryMachines
    results = []
    global NUM_MODEL
    print("queryMachines", len(queryMachines))
    for qMachine in queryMachines:
        for i in range(NUM_MODEL):
            names = qMachine.upsearch(src_name,i, int(k))
            adds = []
            for i, name in enumerate(names):
                info = {}

                info["value"] = name
                adds.append(info)
            print(adds)
            results.append(adds)

        # results.append(qMachine.search(src_type, src_name, target_type,int(k)))

    return jsonify(results), 200

@app.route("/api/downsearch/<src_name>/<k>", methods=["GET"])
def downsearch(src_name, k):
    results = []
    global NUM_MODEL
    global queryMachines
    print("queryMachines", len(queryMachines))
    for qMachine in queryMachines:
        for i in range(NUM_MODEL):
            names = qMachine.downsearch(src_name,i, int(k))
            adds = []
            for i, name in enumerate(names):
                info = {}

                info["value"] = name
                adds.append(info)
            print(adds)
            results.append(adds)

        # results.append(qMachine.search(src_type, src_name, target_type,int(k)))

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(debug=True)