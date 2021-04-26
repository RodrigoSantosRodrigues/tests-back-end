def custom_reponse(response, status_code):
    return {
        'status': status_code,
        'body': response
    }
