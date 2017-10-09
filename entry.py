class FieldProp(object):
    def __init__(self, ttype, required=False):
        self.ttype = ttype
        self.required = required


class Entry(object):

    KNOWN_FIELDS = {
        'name': FieldProp(str, True),
        'account': FieldProp(str, True),
        'passwd': FieldProp(str, True),
        'email': FieldProp(str),
        'alt_email': FieldProp(list),
    }

    def __init__(self, **kwargs):
        for field, prop in self.KNOWN_FIELDS.items():
            value = kwargs.get(field, None)
            if prop.required and not value:
                raise ValueError('{} is required'.format(field))
            if not prop.required and not value:
                setattr(self, field, value)
                if field in kwargs:
                    kwargs.pop(field)
                continue
            if prop.ttype != type(value):
                raise ValueError(
                    '{} requires type {}'.format(
                        field,
                        prop.ttype,
                    ),
                )
            setattr(self, field, value)
            kwargs.pop(field)
        if kwargs:
            raise ValueError('Unknown fields {}'.format(kwargs))

    def echo_basic_entry(self, account_key, passwd_key, email_key):
        print('name: ', self.name)
        print('account: ', self.account.format(**account_key))
        print('passwd: ', self.passwd.format(**passwd_key))
        if self.email:
            print('email: ', self.email.format(**email_key))
        else:
            print('email: ', None)
        if self.alt_email:
            fmt_alt_email = [
                email.format(**email_key) for email in self.alt_email
            ]
            print('alt_email: ', fmt_alt_email)
        else:
            print('alt_email: ', None)


class BankEntry(Entry):

    KNOWN_FIELDS = {
        'name': FieldProp(str, True),
        'account': FieldProp(str, True),
        'passwd': FieldProp(str, True),
        'email': FieldProp(str),
        'sec_question': FieldProp(dict),
        'accountn': FieldProp(str),
        'alt_email': FieldProp(list),
        'url': FieldProp(list),
        'pin': FieldProp(str),
    }


class MilEntry(Entry):

    KNOWN_FIELDS = {
        'name': FieldProp(str, True),
        'account': FieldProp(str, True),
        'passwd': FieldProp(str, True),
        'email': FieldProp(str),
        'alt_email': FieldProp(list),
        'sec_question': FieldProp(dict),
        'cac_pin': FieldProp(str),
        'security_img': FieldProp(str),
    }


class WebEntry(Entry):

    KNOWN_FIELDS = {
        'name': FieldProp(str, True),
        'account': FieldProp(str, True),
        'passwd': FieldProp(str, True),
        'email': FieldProp(str),
        'sec_question': FieldProp(dict),
        'alt_email': FieldProp(list),
    }


class MedicalEntry(Entry):

    KNOWN_FIELDS = {
        'name': FieldProp(str, True),
        'account': FieldProp(str, True),
        'passwd': FieldProp(str, True),
        'email': FieldProp(str),
        'alt_email': FieldProp(list),
        'accountn': FieldProp(str),
        'url': FieldProp(list),
        'sec_question': FieldProp(dict),
    }
