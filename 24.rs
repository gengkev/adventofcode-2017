use std::env;
use std::collections::HashMap;
use std::collections::hash_map::RandomState;
use std::collections::VecDeque;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::process::exit;
use std::time::Instant;

type PipeChain = Vec<(i32, i32)>;
type PipeMap = HashMap<i32, PipeChain, RandomState>;

fn solve1(map: &PipeMap) {
    let mut best_strength_1 = 0;
    let mut best_len = 0;
    let mut best_strength = 0;

    let mut q = VecDeque::new();
    q.push_back((0, 0, Vec::new()));

    while let Some((c, s, chain)) = q.pop_front() {
        //eprintln!("{} {} {:?}", c, s, chain);

        // Star 1
        if s > best_strength_1 {
            best_strength_1 = s;
        }

        // Star 2
        if (chain.len(), s) > (best_len, best_strength) {
            best_len = chain.len();
            best_strength = s;
        }

        for &n in &map[&c] {
            if chain.contains(&n) { continue; }
            if n.0 != c && n.1 != c { continue; }
            let d = if c == n.0 { n.1 } else { n.0 };

            let mut nchain: PipeChain = chain.clone();
            nchain.push(n);
            q.push_back((d, s+c+d, nchain));
        }
    }

    println!("Star 1: {}", best_strength_1);
    println!("Star 2: {}", best_strength);
}


fn solve2_helper(map: &PipeMap, c: i32, s: i32, chain: &mut PipeChain)
        -> (i32, (usize, i32)) {
    let mut bs1 = 0;
    let mut bs2 = (0, 0);

    // Star 1
    if s > bs1 {
        bs1 = s;
    }

    // Star 2
    if (chain.len(), s) > bs2 {
        bs2 = (chain.len(), s);
    }

    for &n in &map[&c] {
        if chain.contains(&n) { continue; }
        if n.0 != c && n.1 != c { continue; }
        let d = if c == n.0 { n.1 } else { n.0 };

        chain.push(n);
        let (s1, s2) = solve2_helper(map, d, s+c+d, chain);
        if s1 > bs1 { bs1 = s1; }
        if s2 > bs2 { bs2 = s2; }
        let old_n = chain.pop().unwrap();
        assert!(n == old_n);
    }

    return (bs1, bs2);
}


fn solve2(map: &PipeMap) {
    let (bs1, bs2) = solve2_helper(map, 0, 0, &mut Vec::new());
    println!("Star 1: {}", bs1);
    println!("Star 2: {}", bs2.1);
}


fn main() {
    let mut args = env::args();
    if args.len() != 2 {
        eprintln!("Wrong number of arguments (pass input filename)");
        exit(-1);
    }

    let filename = args.nth(1).unwrap();
    let f = File::open(filename).unwrap();
    let reader = BufReader::new(f);

    let mut map = HashMap::new();
    for line in reader.lines() {
        let line = line.unwrap();
        let mut it = line.split('/');
        let a: i32 = it.next().unwrap().parse().unwrap();
        let b: i32 = it.next().unwrap().parse().unwrap();
        map.entry(a).or_insert_with(Vec::new).push((a, b));
        map.entry(b).or_insert_with(Vec::new).push((a, b));
    }

    println!("Running solve1:");
    let start = Instant::now();
    solve1(&map);
    println!("{:?}", start.elapsed());
    println!();

    println!("Running solve2:");
    let start = Instant::now();
    solve2(&map);
    println!("{:?}", start.elapsed());
}


