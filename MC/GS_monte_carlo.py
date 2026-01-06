import sys

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate_self_avoiding_walk(chain_length, rng, max_restarts=2000):
    """Generate a 3D self-avoiding walk on a cubic lattice."""
    directions = np.array(
        [
            [1, 0, 0],
            [-1, 0, 0],
            [0, 1, 0],
            [0, -1, 0],
            [0, 0, 1],
            [0, 0, -1],
        ],
        dtype=int,
    )
    for _ in range(max_restarts):
        positions = np.zeros((chain_length, 3), dtype=int)
        occupied = {(0, 0, 0)}
        for i in range(1, chain_length):
            moved = False
            for step in directions[rng.permutation(len(directions))]:
                candidate = positions[i - 1] + step
                key = (int(candidate[0]), int(candidate[1]), int(candidate[2]))
                if key not in occupied:
                    positions[i] = candidate
                    occupied.add(key)
                    moved = True
                    break
            if not moved:
                break
        else:
            return positions.astype(float)
    raise RuntimeError(
        f"Failed to generate a self-avoiding walk for N={chain_length}. "
        "Increase --max-restarts or reduce chain length."
    )


def radius_of_gyration(positions):
    center = positions.mean(axis=0)
    r_g = np.sqrt(((positions - center) ** 2).sum(axis=1).mean())
    return r_g


def end_to_end_distance(positions):
    e2e = float(np.linalg.norm(positions[-1] - positions[0]))
    return e2e 


def run_simulation(chain_lengths, n_chains, seed, max_restarts):
    rng = np.random.default_rng(seed)
    results = []
    for n in chain_lengths:
        rgs = []
        e2es = []
        for _ in range(n_chains):
            positions = generate_self_avoiding_walk(n, rng, max_restarts=max_restarts)
            rgs.append(radius_of_gyration(positions))
            e2es.append(end_to_end_distance(positions))
        results.append(
            {
                "N": n,
                "rg_mean": float(np.mean(rgs)),
                "rg_std": float(np.std(rgs, ddof=1)) if n_chains > 1 else 0.0,
                "e2e_mean": float(np.mean(e2es)),
                "e2e_std": float(np.std(e2es, ddof=1)) if n_chains > 1 else 0.0,
            }
        )
    return results


def plot_results(results, show, save_path):
    ns = np.array([row["N"] for row in results])
    rg_mean = np.array([row["rg_mean"] for row in results])
    rg_std = np.array([row["rg_std"] for row in results])
    e2e_mean = np.array([row["e2e_mean"] for row in results])
    e2e_std = np.array([row["e2e_std"] for row in results])

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    axes[0].errorbar(ns, rg_mean, marker="o", capsize=3, label="R_g")
    axes[0].errorbar(
        ns, e2e_mean, marker="s", capsize=3, label="E2E"
    )
    axes[0].set_title("R_g and end-to-end")
    axes[0].set_xlabel("Chain length N")
    axes[0].set_ylabel("Distance")
    # axes[0].legend(frameon=True)

    axes[1].errorbar(ns, rg_mean, yerr=rg_std, marker="o", capsize=3)
    axes[1].set_title("Radius of gyration")
    axes[1].set_xlabel("Chain length N")
    axes[1].set_ylabel("R_g")

    axes[2].errorbar(ns, e2e_mean, yerr=e2e_std, marker="s", color="tab:orange", capsize=3)
    axes[2].set_title("End-to-end distance")
    axes[2].set_xlabel("Chain length N")
    axes[2].set_ylabel("|R_N - R_0|")

    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    if show:
        plt.show()

def plot_polymer_3d(positions, show=True, save_path=""):
    fig = plt.figure(figsize=(6, 5))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], "-o", markersize=3)
    ax.set_title("3D polymer configuration")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.set_box_aspect((1, 1, 1))
    fig.tight_layout()
    if save_path:
        fig.savefig(save_path, dpi=150)
    if show:
        plt.show()


def main(argv):
    rng = np.random.default_rng(0)
    chain_lengths = list(range(10, 81, 10))
    n_chains = 200
    max_restarts = 2000

    results = run_simulation(
        chain_lengths=chain_lengths,
        n_chains=n_chains,
        seed=0,
        max_restarts=max_restarts,
    )

    for row in results:
        print(
            f"N={row['N']:4d}  Rg={row['rg_mean']:.3f} +/- {row['rg_std']:.3f}  "
            f"E2E={row['e2e_mean']:.3f} +/- {row['e2e_std']:.3f}"
        )

    plot_results(results, show=True, save_path="")

    sample_positions = generate_self_avoiding_walk(chain_lengths[-1], rng, max_restarts)
    plot_polymer_3d(sample_positions, show=True, save_path="")


if __name__ == "__main__":
    main(sys.argv[1:])
