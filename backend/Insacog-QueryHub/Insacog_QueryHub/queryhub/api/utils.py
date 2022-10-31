import traceback
import pandas as pd
from colorama import init, Fore
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

init(autoreset=True)


def import_callable(path_or_callable):
    if hasattr(path_or_callable, "__call__"):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, str)
        package, attr = path_or_callable.rsplit(".", 1)
        return getattr(import_module(package), attr)


def generate_response(title, body):
    match title:
        case "non_field_errors":
            msg_head = ""
        case _:
            msg_head = f"{title.capitalize()} :"
    msg_body = (
        body[0].replace(".", "") if (isinstance(body, list)) else body.replace(".", "")
    )
    message = f"{msg_head} {msg_body}".strip()
    return message


def create_uniform_response(errors):
    print("this is printed", errors)
    final_message = []
    if isinstance(errors, list):
        for error in errors:
            for key, value in error.items():
                final_message.append(generate_response(key, value))
    else:
        for key, value in errors.items():
            final_message.append(generate_response(key, value))
    return {"message": "\n".join(final_message), "code": "ERROR"}


def custom_exception_handler(exc, context):
    print("exec and context --", exc, context)
    response = exception_handler(exc, context)
    if response:
        return Response(create_uniform_response(response.data), status=exc.status_code)
    print(f"{Fore.YELLOW}\n\nMessage starts here ------------\n\n")
    print(
        f"{Fore.RED}".join(
            traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        )
    )
    print(f"{Fore.YELLOW}\n\nMessage ends here ------------\n\n")
    message = {
        "code": "ERROR",
        "message": "Error occured, admin has been informed",
    }
    return Response(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def stacked_bar(QuerySet):
    res = QuerySet[0]
    res = list(res.keys())
    mnd = {}
    mnlist = []
    for dic in QuerySet:
        v = dic[res[0]]
        if v not in mnlist:
            mnlist.append(v)
    mnd[res[0]] = mnlist
    df = pd.DataFrame(QuerySet)
    df = df.set_index(res[0])
    dfT = df.T
    req_list = []
    for j in list(dfT.loc[res[1]].unique()):
        t = {}
        t[res[1]] = j
        t["value"] = []
        req_list.append(t)
    df2 = pd.DataFrame(QuerySet)
    df2 = df2.set_index([res[0], res[1]])
    for dic in req_list:
        lndic = dic[res[1]]
        months = mnd[res[0]]
        for month in months:
            if lndic in df2.loc[month].index:
                val = df2.loc[month, lndic][res[2]]
                dic["value"].append(val)
            else:
                dic["value"].append(0)
    return {res[0]: mnd, res[1]: req_list}


def weekly_report_stacked(QuerySet):
    res = QuerySet[0]
    res = list(res.keys())
    mnd = {}
    mnlist = []
    for dic in QuerySet:
        v = dic[res[0]]
        if v not in mnlist:
            mnlist.append(v)
    mnd[res[0]] = mnlist

    df = pd.DataFrame(QuerySet)
    df = df.set_index(res[0])
    dfT = df.T
    req_list = []
    for j in list(dfT.loc[res[1]].unique()):
        t = {}
        t[res[1]] = j
        t["value"] = []
        req_list.append(t)
    df2 = pd.DataFrame(QuerySet)
    df2 = df2.set_index([res[0], res[1]])
    for dic in req_list:
        lndic = dic[res[1]]
        months = mnd[res[0]]
        for month in months:
            if lndic in df2.loc[month].index:
                val = df2.loc[month, lndic][res[2]]
                dic["value"].append(val)
            else:
                dic["value"].append(0)
    c = []

    def column_sums(square):
        for i in req_list:
            c.append(i["value"])
        for j in req_list:
            return [sum(i) for i in zip(*square)]

    c = column_sums(c)
    b = []
    for j in req_list:
        yu = []
        b.append(j["value"])
        j["value1"] = []
        yu = [[round((100 * x / y), 2) for x, y in zip(lst, c)] for lst in b]
        for i in yu:
            j["value1"] = i
    req_list = sorted(req_list, key=lambda d: d["who_label"])
    return {res[0]: mnd, res[1]: req_list}
