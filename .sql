select
T.Id,
T.Nome,
T.TarefaPai,
T.ChecklistId,
T.Escalonado,
T.TerminoReal
from dw_vista.dbo.FT_TAREFA T
inner join dw_vista.dbo.DM_ESTRUTURA Es
    on Es.Id_Estrutura = T.Id_Estrutura
where es.crno= 60433
order by TerminoReal DESC
-- chave
-- 8A950E7C-C59F-4FE6-BAEA-52FDFA2B9112
-- cartão carinho
-- 24B19E8B-D618-45CA-B175-4519F3102F79



