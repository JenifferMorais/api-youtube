create or replace function nome_piloto() returns trigger as
$$
begin 
	update pessoa  set nome = 'Comandante ' || 
	new.nome 
	where pessoa.cpf = new.cpf;
return new;
end;
$$
language plpgsql;


create trigger novo_nome after
insert on pessoa 
for each  row 
execute procedure nome_piloto();


INSERT INTO PESSOA
(cpf, nome, sexo)
VALUES('05284549', 'Jeniffer59988', 'F');

select * from pessoa p;