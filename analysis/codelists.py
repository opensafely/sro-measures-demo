from cohortextractor import codelist_from_csv

sbp_codelist = codelist_from_csv(
    "codelists/opensafely-systolic-blood-pressure-qof.csv",
    system="snomed",
    column="code",
)

home_bp_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-homebp_cod.csv",
    system="snomed",
    column="code",
)
