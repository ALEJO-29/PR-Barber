def total_carro(request):
    total=0
    if request.user.is_authenticated:
        if request.session["carro"]:
            for key, value in request.session["carro"].items():
                total+=total + (float(value["precio"]*value["cantidad"]))
        return {"total_carro": total}