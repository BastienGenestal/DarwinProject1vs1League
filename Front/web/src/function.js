import { i18n } from './i18n/i18n'
import { LANG } from './global'

export const required = value => value ? undefined : i18n[LANG]._form._required_input