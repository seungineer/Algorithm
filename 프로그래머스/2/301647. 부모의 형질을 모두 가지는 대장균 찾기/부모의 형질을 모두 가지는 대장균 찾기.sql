select e.id, e.genotype, d.genotype as parent_genotype
from ecoli_data as e
left outer join
ecoli_data as d
on e.parent_id = d.id
where e.genotype & d.genotype like d.genotype
order by 1