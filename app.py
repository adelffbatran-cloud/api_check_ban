from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/ban', methods=['GET'])
def check_ban():
    uid = request.args.get('uid')
    if not uid:
        return jsonify({"error": "Please provide a uid"}), 400

    # „‰ÿﬁ «·”Ì—›— «·Œ«’ »ﬂ ·›Õ’ «·Õ”«» ⁄»— «·‹ UID
    # (Ì„ﬂ‰ﬂ  ⁄œÌ· Â–« «·„‰ÿﬁ ·«Õﬁ« √Ê —»ÿÂ »«·ÿ—Ìﬁ… «· Ì  ⁄Ã»ﬂ)
    if uid.endswith('0'):
        is_banned = True
        period = "Permanent (œ«∆„)"
        region = "ME («·‘—ﬁ «·√Ê”ÿ)"
    else:
        is_banned = False
        period = "None"
        region = "ME («·‘—ﬁ «·√Ê”ÿ)"

    return jsonify({
        "uid": uid,
        "banned": is_banned,
        "region": region,
        "period": period
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)