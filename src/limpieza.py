import pandas as pd

def rellenar_ocupacion(df):
    df["OCUPACION"] = df["OCUPACION"].fillna("SIN_OCUPACION")
    return df

def rellenar_ratio(df):
    df["RATIO_ENTRE_CUOTA_E_INGRESO_TOTAL"] = df["RATIO_ENTRE_CUOTA_E_INGRESO_TOTAL"].fillna("mean") #Llenamos con la media del ratio del total de registros
    return df

def rellenar_mora_actual(df):
    df["MORA_TOTAL_ACTUAL"] = df["MORA_TOTAL_ACTUAL"].fillna(0) ##LLenamos con 0 ya que son personas que no tienen deuda externa
    return df

def rellenar_promedio_deuda_externa(df):
    df["PROMEDIO_DEUDA_EXTERNA"] = df["PROMEDIO_DEUDA_EXTERNA"].fillna(0) #LLenamos con 0 ya que son personas que no tienen deuda externa
    return df

def rellenar_veces_ha_pedido_prorroga(df):
    df["VECES_QUE_HA_PEDIDO_PRORROGAS"] = df["VECES_QUE_HA_PEDIDO_PRORROGAS"].fillna(0) #LLenamos con 0 ya que son personas que no tienen registro de haber pedido prorrogas
    return df

def rellenar_genero(df):
    df["GENERO"] = df["GENERO"].replace("XNA","F") #El valor XNA lo rellenamos con Femenino ya que son el genero más común
    return df

def reducir_ocupaciones(df):
    df["OCUPACION"] = df["OCUPACION"].map(lambda x: "SIN_OCUPACION" if x =="SIN_OCUPACION" else "CON_OCUPACION").astype("object") #Si es sin ocupacion, dejelo asi, si no, pongalo con ocupacion
    return df