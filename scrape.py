import mechanize

# Config vars
URL = "https://servicioselectronicos.sanidadmadrid.org/LEQ/Consulta.aspx"

if __name__ == "__main__":

    br = mechanize.Browser()
    br.open(URL)
    response = br.response()
    br.select_form('aspnetForm')
    form = br.form

    # Select the second hospital and re-submit in order to have the list of
    # services available in that hospital
    form.controls[2].items[1].selected = True
    request = br.submit()
    # We can now submit with the desired selection
    br.select_form('aspnetForm')
    form = br.form
    form.controls[2].items[1].selected = True
    form.controls[3].items[1].selected = True
    form.controls[4].items[0].selected = True
    req_data = form.click_request_data()
    response = br.submit()
    # TODO: response doesn't contain the desired value. The form is returned
    # with the selected values filled in, but no response is obtained.

    # Another idea: take the req_data string and feed it directly to the form
    # using a requests object. It doesn't work either.
    x = requests.request('POST', 
                         req_data[0], 
                         data = req_data[1], 
                         headers = {req_data[2][0][0]: req_data[2][0][1]})
