
from config.app import *
import pandas as pd
import os

def GenerateReportVentas(app: App):
    conn = app.bd.getConection()
    
    query = """
        SELECT 
            p.pais,
            COUNT(v.sales_amount) AS total_ventas,
            SUM(v.sales_amount) AS total_gastado,
            AVG(v.sales_amount) AS promedio_gasto,
            (
                SELECT v2.product_id
                FROM VENTAS v2
                WHERE v2.postal_code = v.postal_code
                GROUP BY v2.product_id
                ORDER BY SUM(v2.quantity) DESC
                LIMIT 1
            ) AS producto_mas_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p
        ON 
            v.postal_code = p.code
        GROUP BY 
            p.pais
        ORDER BY 
            total_gastado DESC;
    """
    
    df = pd.read_sql_query(query, conn)
    
    # Para que sean más legibles
    df["total_gastado"] = df["total_gastado"].apply(lambda x: f"{x:,.2f}")
    df["promedio_gasto"] = df["promedio_gasto"].apply(lambda x: f"{x:,.2f}")

    # Mostrar los resultados en la terminal
    print(df)

    # Guardar en CSV
    fecha = "08-02"
    directory = "/workspaces/Workspacepy0125v2/proyecto/files"
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    path = f"{directory}/data-{fecha}.csv"
    df.to_csv(path, index=False)

    sendMail(app, path)

def sendMail(app: App, data):
    app.mail.send_email(
        'from@example.com',
        'Reporte de países con mayor gasto',
        'Adjunto el reporte con más detalles: total de ventas, gasto total, promedio de gasto y producto más vendido por país.',
        data
    )
