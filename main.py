from flask import *
from model import QueryMachine
from utils import get_meta_from_json
from collections import defaultdict
import json
# import pymongo

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
query_machine = []  # QueryMachine()
queryMachines = []
@app.route('/')
def upload():
    # return render_template("file_upload_form.html")
    dataFiles = [{
        "id": "model1",
        "metaFile": "Choose file",
        "embFile": "Choose file"
    }]
    return render_template("demo.html", datasets=dataFiles, types=["Empty"], name_dict=[])


def clean(string):
    return string.replace('"', '\\"')
    # to_save = ""
    # for char in string:
    #     if not char.isalpha():
    #         if char != " ":
    #             continue
    #     to_save += char
    # return to_save


@app.route('/success', methods=['POST'])
def success():
    dataFiles = []
    if request.method == 'POST':
        numDatasets = int(request.form['numDatasets'])
        global queryMachines
        queryMachines = []
        # Dictionary from type (comp, tech) to list of comps, techs
        name_dict = {}
        n_dicts = []
        for model in range(numDatasets):
            meta_f = request.files['meta_file_model' + str(model + 1)]
            assert meta_f.filename.endswith('json')
            meta_f.save("temp_" + meta_f.filename)
            n_dict, results = get_meta_from_json("temp_" + meta_f.filename)
            n_dicts.append(n_dict)

            query_machine = QueryMachine()
            query_machine.update_data(results)
            queryMachines.append(query_machine)
            print("qm", len(queryMachines))
            dataFiles.append({
                "id": "model" + str(model + 1),
                "metaFile": meta_f.filename[:-5]
            })
        # Merge n_dict
        com_set = set(n_dict['Company'])
        ent_set = set(n_dict['Tech'])
        # import pdb
        # pdb.set_trace()
        for n_dict in n_dicts:
            com_set.intersection_update(set(n_dict['Company']))
            ent_set.intersection_update(set(n_dict['Tech']))
        name_dict['Company'] = sorted(list(com_set))
        name_dict['Tech'] = sorted(list(ent_set))

        return render_template("demo.html", datasets=dataFiles, types=list(name_dict.keys()), name_dict=name_dict)


@app.route("/api/search/<src_type>/<src_name>/<target_type>/<k>", methods=["GET"])
def search(src_type, src_name, target_type, k):
    # colect = mongo_db['kstn']
    results = []
    print("queryMachines", len(queryMachines))
    for qMachine in queryMachines:
        searches = qMachine.search(src_type, src_name, target_type, int(k))
        adds = []
        for i, s in enumerate(searches):
            info = {}

            info["value"] = s
            info["address"] = i
            adds.append(info)
        results.append(adds)

        # results.append(qMachine.search(src_type, src_name, target_type,int(k)))

    return jsonify(results), 200


if __name__ == '__main__':
    app.run(debug=True)
